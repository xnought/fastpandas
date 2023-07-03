import pandas as pd
import duckdb


class DuckDBOp:
    def __init__(self, func, columns):
        self.func = func
        self.columns = columns

    def compile(self):
        if isinstance(self.columns, list) and (
            self.columns is not None or len(self.columns) > 0
        ):
            compiled = []
            for c in self.columns:
                if isinstance(c, DuckDBOp):
                    compiled.append(c.compile())
                else:
                    compiled.append(c)
            return self.func(*compiled)
        else:
            if isinstance(self.columns, DuckDBOp):
                return self.func(self.columns.compile())
            return self.func(self.columns)

    def compile_where(self):
        return ""

    def item(self, _df):
        where = self.compile_where()
        name = self.compile()
        query = f"""SELECT {name} as result from _df"""
        if where != "":
            query += f" WHERE {where}"
        return duckdb.query(query).df()["result"][0]

    def df(self, _df):
        where = self.compile_where()
        name = self.compile()
        query = f"""SELECT {name} from _df"""
        if where != "":
            query += f" WHERE {where}"
        return duckdb.query(query).df()


if __name__ == "__main__":
    df = pd.DataFrame({"a": list(range(100_000))})
    atom = DuckDBOp(
        lambda a, b,: f"pow({a}, {b})", [DuckDBOp(lambda x: f"{x}*2", ["a"]), 2]
    )
