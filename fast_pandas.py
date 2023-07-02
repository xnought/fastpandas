from lazy import DuckDBUnary


def avg(arg):
	return DuckDBUnary(lambda c: 'avg' + '(' + c + ')', arg)


def bit_and(arg):
	return DuckDBUnary(lambda c: 'bit_and' + '(' + c + ')', arg)


def bit_or(arg):
	return DuckDBUnary(lambda c: 'bit_or' + '(' + c + ')', arg)


def bit_xor(arg):
	return DuckDBUnary(lambda c: 'bit_xor' + '(' + c + ')', arg)


def bool_and(arg):
	return DuckDBUnary(lambda c: 'bool_and' + '(' + c + ')', arg)


def bool_or(arg):
	return DuckDBUnary(lambda c: 'bool_or' + '(' + c + ')', arg)


def count(arg):
	return DuckDBUnary(lambda c: 'count' + '(' + c + ')', arg)


def first(arg):
	return DuckDBUnary(lambda c: 'first' + '(' + c + ')', arg)


def histogram(arg):
	return DuckDBUnary(lambda c: 'histogram' + '(' + c + ')', arg)


def last(arg):
	return DuckDBUnary(lambda c: 'last' + '(' + c + ')', arg)


def list(arg):
	return DuckDBUnary(lambda c: 'list' + '(' + c + ')', arg)


def max(arg):
	return DuckDBUnary(lambda c: 'max' + '(' + c + ')', arg)


def min(arg):
	return DuckDBUnary(lambda c: 'min' + '(' + c + ')', arg)


def product(arg):
	return DuckDBUnary(lambda c: 'product' + '(' + c + ')', arg)


def sum(arg):
	return DuckDBUnary(lambda c: 'sum' + '(' + c + ')', arg)


def approx_count_distinct(x):
	return DuckDBUnary(lambda c: 'approx_count_distinct' + '(' + c + ')', x)


def entropy(x):
	return DuckDBUnary(lambda c: 'entropy' + '(' + c + ')', x)


def kurtosis(x):
	return DuckDBUnary(lambda c: 'kurtosis' + '(' + c + ')', x)


def mode(x):
	return DuckDBUnary(lambda c: 'mode' + '(' + c + ')', x)


def skewness(x):
	return DuckDBUnary(lambda c: 'skewness' + '(' + c + ')', x)


def stddev_pop(x):
	return DuckDBUnary(lambda c: 'stddev_pop' + '(' + c + ')', x)


def stddev_samp(x):
	return DuckDBUnary(lambda c: 'stddev_samp' + '(' + c + ')', x)


def var_pop(x):
	return DuckDBUnary(lambda c: 'var_pop' + '(' + c + ')', x)


def var_samp(x):
	return DuckDBUnary(lambda c: 'var_samp' + '(' + c + ')', x)


def abs(x):
	return DuckDBUnary(lambda c: 'abs' + '(' + c + ')', x)


def acos(x):
	return DuckDBUnary(lambda c: 'acos' + '(' + c + ')', x)


def bit_count(x):
	return DuckDBUnary(lambda c: 'bit_count' + '(' + c + ')', x)


def cbrt(x):
	return DuckDBUnary(lambda c: 'cbrt' + '(' + c + ')', x)


def ceil(x):
	return DuckDBUnary(lambda c: 'ceil' + '(' + c + ')', x)


def chr(x):
	return DuckDBUnary(lambda c: 'chr' + '(' + c + ')', x)


def cos(x):
	return DuckDBUnary(lambda c: 'cos' + '(' + c + ')', x)


def cot(x):
	return DuckDBUnary(lambda c: 'cot' + '(' + c + ')', x)


def degrees(x):
	return DuckDBUnary(lambda c: 'degrees' + '(' + c + ')', x)


def floor(x):
	return DuckDBUnary(lambda c: 'floor' + '(' + c + ')', x)


def ln(x):
	return DuckDBUnary(lambda c: 'ln' + '(' + c + ')', x)


def log(x):
	return DuckDBUnary(lambda c: 'log' + '(' + c + ')', x)


def log2(x):
	return DuckDBUnary(lambda c: 'log2' + '(' + c + ')', x)


def pi():
	return DuckDBUnary(lambda c: 'pi' + '(' + c + ')', )


def radians(x):
	return DuckDBUnary(lambda c: 'radians' + '(' + c + ')', x)


def sin(x):
	return DuckDBUnary(lambda c: 'sin' + '(' + c + ')', x)


def sign(x):
	return DuckDBUnary(lambda c: 'sign' + '(' + c + ')', x)


def sqrt(x):
	return DuckDBUnary(lambda c: 'sqrt' + '(' + c + ')', x)


def tan(x):
	return DuckDBUnary(lambda c: 'tan' + '(' + c + ')', x)

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

	def df(self):
		return self.graph.df(self.dataframe)

	def item(self):
		return self.graph.item(self.dataframe)

	def __repr__(self) -> str:
		return self.graph.compile()

	def avg(self):
		return FastPandas(self.dataframe, avg(self.graph))

	def bit_and(self):
		return FastPandas(self.dataframe, bit_and(self.graph))

	def bit_or(self):
		return FastPandas(self.dataframe, bit_or(self.graph))

	def bit_xor(self):
		return FastPandas(self.dataframe, bit_xor(self.graph))

	def bool_and(self):
		return FastPandas(self.dataframe, bool_and(self.graph))

	def bool_or(self):
		return FastPandas(self.dataframe, bool_or(self.graph))

	def count(self):
		return FastPandas(self.dataframe, count(self.graph))

	def first(self):
		return FastPandas(self.dataframe, first(self.graph))

	def histogram(self):
		return FastPandas(self.dataframe, histogram(self.graph))

	def last(self):
		return FastPandas(self.dataframe, last(self.graph))

	def list(self):
		return FastPandas(self.dataframe, list(self.graph))

	def max(self):
		return FastPandas(self.dataframe, max(self.graph))

	def min(self):
		return FastPandas(self.dataframe, min(self.graph))

	def product(self):
		return FastPandas(self.dataframe, product(self.graph))

	def sum(self):
		return FastPandas(self.dataframe, sum(self.graph))

	def approx_count_distinct(self):
		return FastPandas(self.dataframe, approx_count_distinct(self.graph))

	def entropy(self):
		return FastPandas(self.dataframe, entropy(self.graph))

	def kurtosis(self):
		return FastPandas(self.dataframe, kurtosis(self.graph))

	def mode(self):
		return FastPandas(self.dataframe, mode(self.graph))

	def skewness(self):
		return FastPandas(self.dataframe, skewness(self.graph))

	def stddev_pop(self):
		return FastPandas(self.dataframe, stddev_pop(self.graph))

	def stddev_samp(self):
		return FastPandas(self.dataframe, stddev_samp(self.graph))

	def var_pop(self):
		return FastPandas(self.dataframe, var_pop(self.graph))

	def var_samp(self):
		return FastPandas(self.dataframe, var_samp(self.graph))

	def abs(self):
		return FastPandas(self.dataframe, abs(self.graph))

	def acos(self):
		return FastPandas(self.dataframe, acos(self.graph))

	def bit_count(self):
		return FastPandas(self.dataframe, bit_count(self.graph))

	def cbrt(self):
		return FastPandas(self.dataframe, cbrt(self.graph))

	def ceil(self):
		return FastPandas(self.dataframe, ceil(self.graph))

	def chr(self):
		return FastPandas(self.dataframe, chr(self.graph))

	def cos(self):
		return FastPandas(self.dataframe, cos(self.graph))

	def cot(self):
		return FastPandas(self.dataframe, cot(self.graph))

	def degrees(self):
		return FastPandas(self.dataframe, degrees(self.graph))

	def floor(self):
		return FastPandas(self.dataframe, floor(self.graph))

	def ln(self):
		return FastPandas(self.dataframe, ln(self.graph))

	def log(self):
		return FastPandas(self.dataframe, log(self.graph))

	def log2(self):
		return FastPandas(self.dataframe, log2(self.graph))

	def pi(self):
		return FastPandas(self.dataframe, pi(self.graph))

	def radians(self):
		return FastPandas(self.dataframe, radians(self.graph))

	def sin(self):
		return FastPandas(self.dataframe, sin(self.graph))

	def sign(self):
		return FastPandas(self.dataframe, sign(self.graph))

	def sqrt(self):
		return FastPandas(self.dataframe, sqrt(self.graph))

	def tan(self):
		return FastPandas(self.dataframe, tan(self.graph))

