import pandas as pd
import duckdb


class DuckDBAtom:
    def __init__(self, func, column):
        self.func = func
        self.column = column

    def result(self):
        if isinstance(self.column, DuckDBAtom):
            return self.func(self.column.result())
        return self.func(self.column)

    def agg(self, _df):
        name = self.result()
        query = f"""SELECT {name} as result from _df"""
        return duckdb.query(query).df()["result"][0]

    def full(self, _df):
        name = self.result()
        query = f"""SELECT {name} from _df"""
        return duckdb.query(query).df()


def entropy(column):
    return DuckDBAtom(lambda c: f"entropy({c})", column)


def avg(column: DuckDBAtom):
    return DuckDBAtom(lambda c: f"avg({c})", column)


def mult(column: DuckDBAtom, n: float):
    return DuckDBAtom(lambda c: f"{c}*{n}", column)


class FastPandas:
    def __init__(self, dataframe, graph=None):
        self.dataframe = dataframe
        self.graph = graph

    def __getitem__(self, item):
        return self.column(item)

    def column(self, name):
        if name in self.dataframe.columns:
            return FastPandas(self.dataframe, DuckDBAtom(lambda c: c, name))
        else:
            raise KeyError(f"{name} not in columns")

    def approx_count_distinct(self):
        return FastPandas(
            df, DuckDBAtom(lambda c: f"approx_count_distinct({c})", self.graph)
        ).item()

    def mult(self, other):
        return FastPandas(df, mult(self.graph, other))

    def add(self, other):
        return FastPandas(df, DuckDBAtom(lambda c: f"{c}+{other}", self.graph))

    def entropy(self):
        return FastPandas(df, entropy(self.graph)).item()

    def avg(self):
        return FastPandas(df, avg(self.graph)).item()

    def df(self):
        return self.graph.full(self.dataframe)

    def item(self):
        return self.graph.agg(self.dataframe)


if __name__ == "__main__":
    df = pd.DataFrame({"a": list(range(100_000))})
    fastdf = FastPandas(df)
    result = fastdf["a"].add(25).mult(2).avg()
    print(result)
