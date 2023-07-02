# FastPandas

Extremely fast functions for pandas dataframes built on top of DuckDB.

This library is so low effort, I have to tell more. I literally compile SQL DuckDB queries into a high level API thats easy to use with pandas.

Most of the aggregate and numeric functions are supported. Please check out the [DuckDB docs](https://duckdb.org/docs/sql) for more information. Or check out the compiled code at [`fast_pandas.py`](fast_pandas.py).

Anything listed on the [DuckDB Numeric docs](https://duckdb.org/docs/archive/0.2.9/sql/functions/numeric) and [DuckDB Aggregate docs](https://duckdb.org/docs/archive/0.2.9/sql/aggregates) is supported including nice statistical functions that scale to large amounts of data.

## Usage

Check out [`example.ipynb`](example.ipynb) for real examples you can run through.

Or stay here.

**Lazy Evaluation**

FastPandas is lazy. Meaning you chain your desired operations, and the value is only computed when you actually request the data (with `.item()` or `.df()`).

For example, to average over the dataframes "a" column you could do

```python
from fast_pandas import FastPandas

df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

output = FastPandas(df)["a"].avg()
print(output.item())
#  5.5
```

**Or if you have more complex operations**

Like if I wanted to multiply two columns, then absolute value the result, then add 1, then compute the entropy of that column, I could do

```python
df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'b': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]})

output = FastPandas(df)["a"].mul(FastPandas(df)["b"]).abs().add(1).entropy()
print(output.item())
# 2.321928094887362
```

Which essentially lazily fuses the operations into a single SQL query which is insanely fast on DuckDB.

**Or if you want to approximately count the number of unique values in a column**

Use DuckDB's hyperloglog implementation!!!

first create a df, this one has 100 million rows!

```python
import random
large_df = pd.DataFrame({"a": random.choices(range(35_000_000), k=100_000_000)})
```

Then easily use a [DuckDB Aggregate](https://duckdb.org/docs/archive/0.2.9/sql/aggregates) function like `approx_count_distinct` to count the number of unique elements in the column (roughly).

```python
unique_elements = FastPandas(large_df)["a"].approx_count_distinct()
print(unique_elements.item()) # uses hyperloglog under the hood and took 0.1 seconds
```
