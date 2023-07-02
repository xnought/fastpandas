import pandas as pd
import duckdb


class DuckDBUnary:
    def __init__(self, func, columns):
        self.func = func
        self.columns = columns

    def compile(self):
        if isinstance(self.columns, list) and (
            self.columns is not None or len(self.columns) > 0
        ):
            compiled = []
            for c in self.columns:
                if isinstance(c, DuckDBUnary):
                    compiled.append(c.compile())
                else:
                    compiled.append(c)
            print(compiled)
            return self.func(*compiled)
        else:
            if isinstance(self.columns, DuckDBUnary):
                return self.func(self.columns.compile())
            return self.func(self.columns)

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
    atom = DuckDBUnary(
        lambda a, b,: f"pow({a}, {b})", [DuckDBUnary(lambda x: f"{x}*2", ["a"]), 2]
    )
    print(atom.compile())
