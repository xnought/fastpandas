import duckdb


def approx_count_distinct(_df, column):
    query = f"""SELECT approx_count_distinct({column}) as result from _df"""
    return duckdb.query(query).df()["result"][0]
