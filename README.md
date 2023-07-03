# FastPandas

Lazy evaluation with DuckDB for lighting fast pandas functions. Scales to hundreds of millions of data in fractions of a second!

Includes tons of

-   [numeric functions](https://duckdb.org/docs/archive/0.2.9/sql/functions/numeric)
-   [aggregate functions (statistical, approximate, and more)](https://duckdb.org/docs/archive/0.2.9/sql/aggregates)
-   [filtering](https://duckdb.org/docs/archive/0.2.9/sql/expressions/comparison_operators)

To find the exact functions, go to the compiled code [`fastpandas.py`](fastpandas.py).

## What is the library? And why lazy?

DuckDB runs SQL and is extremely fast. Like really really really fast.

This library makes it easy to run DuckDB on your pandas dataframes.

It works by selecting a column in your dataframe `df`

```python
df = pd.DataFrame() # with your own data
FastPandas(df)["column_in_df"]
```

and applying numeric functions and aggregate functions.

For example taking the natural log, squaring, then averaging.

```python
df = pd.DataFrame() # with your own data
output = FastPandas(df)["column_in_df"].ln().pow(2).avg()
```

But nothing is computed yet! Only when you need the value, the entire chain is fused together, then executed all at once

```python
df = pd.DataFrame() # with your own data
output = FastPandas(df)["column_in_df"].ln().pow(2).avg() # not executed yet

print(output.item()) # NOW gets executed with .item()
```

There is no need to compute them separetly, then combine. Just run'em all at once! We love being lazy!

## Usage

Check out [`example.ipynb`](example.ipynb) for real examples you can run through or continue.

**Installation**

```bash
git clone https://github.com/xnought/fastpandas.git
cd fastpandas
pip3 install -r requirements.txt
```

**Lazy Evaluation**

FastPandas is lazy. Meaning you chain your desired operations, and the value is only computed when you actually request the data (with `.item()` or `.df()`).

For example, to average over the dataframes "a" column you could do

```python
from fastpandas import FastPandas

df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

output = FastPandas(df)["a"].avg()
print(output.item())
#  5.5
```

If you would rather output the entire dataframe (ie you never applied an aggregate function), use `.df()` instead of `.item()`.

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

**Filtering**

If you want to also filter down, you can do that. Note that the last `.filter()` will be the only one applied.

For example, if I want all the values in column "a" that are greater than 1 and summed up, I could do

```python
FastPandas(large_df)["a"].filter(FastPandas(large_df)["a"].gt(1)).sum().item()
```

If I wanted all the values less than 0 and greater than 1 summed up, I could do

```python
_filter = FastPandas(large_df)["a"].lt(0)._and(FastPandas(large_df)["a"].gt(1))
FastPandas(large_df)["a"].filter(_filter).sum().item()
```

Or going back to the counting unique elements if I wanted to counted the number of unique elements between 0 and 10,

```python
between_0_and_10 = FastPandas(large_df)["a"].gte(0)._and(FastPandas(large_df)["b"].lte(10))
FastPandas(large_df)["a"].filter(between_0_and_10).approx_count_distinct().item()
```
