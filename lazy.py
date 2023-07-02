import pandas as pd
import duckdb


class DuckDBUnary:
    def __init__(self, func, column):
        self.func = func
        self.column = column

    def compile(self):
        if isinstance(self.column, DuckDBUnary):
            return self.func(self.column.compile())
        return self.func(self.column)

    def item(self, _df):
        name = self.compile()
        query = f"""SELECT {name} as result from _df"""
        return duckdb.query(query).df()["result"][0]

    def df(self, _df):
        name = self.compile()
        query = f"""SELECT {name} from _df"""
        return duckdb.query(query).df()


def entropy(column):
    return DuckDBUnary(lambda c: f"entropy({c})", column)


def avg(column: DuckDBUnary):
    return DuckDBUnary(lambda c: f"avg({c})", column)


def mult(column: DuckDBUnary, n: float):
    return DuckDBUnary(lambda c: f"({c}*{n})", column)


class FastPandas:
    def __init__(self, dataframe, graph=None):
        self.dataframe = dataframe
        self.graph = graph

    def __getitem__(self, item):
        return self.column(item)

    def column(self, name):
        if name in self.dataframe.columns:
            return FastPandas(self.dataframe, DuckDBUnary(lambda c: c, f'"{name}"'))
        else:
            raise KeyError(f"{name} not in columns")

    def approx_count_distinct(self):
        return FastPandas(
            df, DuckDBUnary(lambda c: f"approx_count_distinct({c})", self.graph)
        )

    def mult(self, other):
        return FastPandas(df, mult(self.graph, other))

    def add(self, other):
        return FastPandas(df, DuckDBUnary(lambda c: f"({c}+{other})", self.graph))

    def entropy(self):
        return FastPandas(df, entropy(self.graph))

    def avg(self):
        return FastPandas(df, avg(self.graph))

    def df(self):
        return self.graph.df(self.dataframe)

    def item(self):
        return self.graph.item(self.dataframe)

    def __repr__(self) -> str:
        return self.graph.compile()


if __name__ == "__main__":
    df = pd.DataFrame({"a": list(range(100_000))})
    result = FastPandas(df)["a"].add(25).mult(2).avg()
    print(result, result.item())
