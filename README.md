# fast-pandas

This library literally just uses duckdb sql. No effort on my side, but still helpful.

This library takes the aggregate functions from [DuckDB](https://duckdb.org/docs/archive/0.2.9/sql/aggregates.html) and compiles them into easy to use python functions.

## Usage

```python
from fast_pandas import FastPandas

df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

# subtract the average a from each a value, then sum along a
a = FastPandas(df)["a"]
sub_avg_sum = a.sub(a.avg()).sum()
print(sub_avg_sum.item())
```
