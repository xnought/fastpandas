# fast-pandas

This library literally just uses duckdb sql. No effort on myside, but still helpful.

This library takes the aggregate functions from [DuckDB](https://duckdb.org/docs/archive/0.2.9/sql/aggregates.html) and compiles them into easy to use python functions.

## TODO

Lazy composition

Compose duckdb queries easily and they only execute when you call `.result()` to fuse together the operations.

```py
result = avg(mult(_df, 2)).result()
```
