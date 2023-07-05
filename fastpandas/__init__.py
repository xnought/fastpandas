import duckdb
from .lazy import DuckDBOp

def avg(arg):
	return DuckDBOp(lambda arg: 'avg' + '(' + f'{arg}' + ')', arg)

def bit_and(arg):
	return DuckDBOp(lambda arg: 'bit_and' + '(' + f'{arg}' + ')', arg)

def bit_or(arg):
	return DuckDBOp(lambda arg: 'bit_or' + '(' + f'{arg}' + ')', arg)

def bit_xor(arg):
	return DuckDBOp(lambda arg: 'bit_xor' + '(' + f'{arg}' + ')', arg)

def bool_and(arg):
	return DuckDBOp(lambda arg: 'bool_and' + '(' + f'{arg}' + ')', arg)

def bool_or(arg):
	return DuckDBOp(lambda arg: 'bool_or' + '(' + f'{arg}' + ')', arg)

def count(arg):
	return DuckDBOp(lambda arg: 'count' + '(' + f'{arg}' + ')', arg)

def first(arg):
	return DuckDBOp(lambda arg: 'first' + '(' + f'{arg}' + ')', arg)

def histogram(arg):
	return DuckDBOp(lambda arg: 'histogram' + '(' + f'{arg}' + ')', arg)

def last(arg):
	return DuckDBOp(lambda arg: 'last' + '(' + f'{arg}' + ')', arg)

def list(arg):
	return DuckDBOp(lambda arg: 'list' + '(' + f'{arg}' + ')', arg)

def max(arg):
	return DuckDBOp(lambda arg: 'max' + '(' + f'{arg}' + ')', arg)

def min(arg):
	return DuckDBOp(lambda arg: 'min' + '(' + f'{arg}' + ')', arg)

def product(arg):
	return DuckDBOp(lambda arg: 'product' + '(' + f'{arg}' + ')', arg)

def string_agg(arg, sep):
	return DuckDBOp(lambda arg, sep: 'string_agg' + '(' + f'{arg}, {sep}' + ')', [arg, sep])

def sum(arg):
	return DuckDBOp(lambda arg: 'sum' + '(' + f'{arg}' + ')', arg)

def approx_count_distinct(x):
	return DuckDBOp(lambda x: 'approx_count_distinct' + '(' + f'{x}' + ')', x)

def approx_quantile(x,pos):
	return DuckDBOp(lambda x, pos: 'approx_quantile' + '(' + f'{x}, {pos}' + ')', [x, pos])

def reservoir_quantile(x,quantile,sample_size):
	return DuckDBOp(lambda x, quantile, sample_size: 'reservoir_quantile' + '(' + f'{x}, {quantile}, {sample_size}' + ')', [x, quantile, sample_size])

def corr(y,x):
	return DuckDBOp(lambda y, x: 'corr' + '(' + f'{y}, {x}' + ')', [y, x])

def covar_pop(y,x):
	return DuckDBOp(lambda y, x: 'covar_pop' + '(' + f'{y}, {x}' + ')', [y, x])

def entropy(x):
	return DuckDBOp(lambda x: 'entropy' + '(' + f'{x}' + ')', x)

def kurtosis(x):
	return DuckDBOp(lambda x: 'kurtosis' + '(' + f'{x}' + ')', x)

def mode(x):
	return DuckDBOp(lambda x: 'mode' + '(' + f'{x}' + ')', x)

def quantile_cont(x,pos):
	return DuckDBOp(lambda x, pos: 'quantile_cont' + '(' + f'{x}, {pos}' + ')', [x, pos])

def quantile_disc(x,pos):
	return DuckDBOp(lambda x, pos: 'quantile_disc' + '(' + f'{x}, {pos}' + ')', [x, pos])

def regr_avgx(y,x):
	return DuckDBOp(lambda y, x: 'regr_avgx' + '(' + f'{y}, {x}' + ')', [y, x])

def regr_avgy(y,x):
	return DuckDBOp(lambda y, x: 'regr_avgy' + '(' + f'{y}, {x}' + ')', [y, x])

def regr_count(y,x):
	return DuckDBOp(lambda y, x: 'regr_count' + '(' + f'{y}, {x}' + ')', [y, x])

def regr_intercept(y,x):
	return DuckDBOp(lambda y, x: 'regr_intercept' + '(' + f'{y}, {x}' + ')', [y, x])

def regr_r2(y,x):
	return DuckDBOp(lambda y, x: 'regr_r2' + '(' + f'{y}, {x}' + ')', [y, x])

def regr_slope(y,x):
	return DuckDBOp(lambda y, x: 'regr_slope' + '(' + f'{y}, {x}' + ')', [y, x])

def regr_sxx(y,x):
	return DuckDBOp(lambda y, x: 'regr_sxx' + '(' + f'{y}, {x}' + ')', [y, x])

def regr_sxy(y,x):
	return DuckDBOp(lambda y, x: 'regr_sxy' + '(' + f'{y}, {x}' + ')', [y, x])

def regr_syy(y,x):
	return DuckDBOp(lambda y, x: 'regr_syy' + '(' + f'{y}, {x}' + ')', [y, x])

def skewness(x):
	return DuckDBOp(lambda x: 'skewness' + '(' + f'{x}' + ')', x)

def stddev_pop(x):
	return DuckDBOp(lambda x: 'stddev_pop' + '(' + f'{x}' + ')', x)

def stddev_samp(x):
	return DuckDBOp(lambda x: 'stddev_samp' + '(' + f'{x}' + ')', x)

def var_pop(x):
	return DuckDBOp(lambda x: 'var_pop' + '(' + f'{x}' + ')', x)

def var_samp(x):
	return DuckDBOp(lambda x: 'var_samp' + '(' + f'{x}' + ')', x)

def abs(x):
	return DuckDBOp(lambda x: 'abs' + '(' + f'{x}' + ')', x)

def acos(x):
	return DuckDBOp(lambda x: 'acos' + '(' + f'{x}' + ')', x)

def asin(x):
	return DuckDBOp(lambda x: 'asin' + '(' + f'{x}' + ')', x)

def atan(x):
	return DuckDBOp(lambda x: 'atan' + '(' + f'{x}' + ')', x)

def atan2(x, y):
	return DuckDBOp(lambda x, y: 'atan2' + '(' + f'{x}, {y}' + ')', [x, y])

def bit_count(x):
	return DuckDBOp(lambda x: 'bit_count' + '(' + f'{x}' + ')', x)

def cbrt(x):
	return DuckDBOp(lambda x: 'cbrt' + '(' + f'{x}' + ')', x)

def ceil(x):
	return DuckDBOp(lambda x: 'ceil' + '(' + f'{x}' + ')', x)

def ceiling(x):
	return DuckDBOp(lambda x: 'ceiling' + '(' + f'{x}' + ')', x)

def cos(x):
	return DuckDBOp(lambda x: 'cos' + '(' + f'{x}' + ')', x)

def cot(x):
	return DuckDBOp(lambda x: 'cot' + '(' + f'{x}' + ')', x)

def degrees(x):
	return DuckDBOp(lambda x: 'degrees' + '(' + f'{x}' + ')', x)

def even(x):
	return DuckDBOp(lambda x: 'even' + '(' + f'{x}' + ')', x)

def factorial(x):
	return DuckDBOp(lambda x: 'factorial' + '(' + f'{x}' + ')', x)

def floor(x):
	return DuckDBOp(lambda x: 'floor' + '(' + f'{x}' + ')', x)

def gamma(x):
	return DuckDBOp(lambda x: 'gamma' + '(' + f'{x}' + ')', x)

def gcd(x, y):
	return DuckDBOp(lambda x, y: 'gcd' + '(' + f'{x}, {y}' + ')', [x, y])

def greatest_common_divisor(x, y):
	return DuckDBOp(lambda x, y: 'greatest_common_divisor' + '(' + f'{x}, {y}' + ')', [x, y])

def isfinite(x):
	return DuckDBOp(lambda x: 'isfinite' + '(' + f'{x}' + ')', x)

def isinf(x):
	return DuckDBOp(lambda x: 'isinf' + '(' + f'{x}' + ')', x)

def isnan(x):
	return DuckDBOp(lambda x: 'isnan' + '(' + f'{x}' + ')', x)

def lcm(x, y):
	return DuckDBOp(lambda x, y: 'lcm' + '(' + f'{x}, {y}' + ')', [x, y])

def least_common_multiple(x, y):
	return DuckDBOp(lambda x, y: 'least_common_multiple' + '(' + f'{x}, {y}' + ')', [x, y])

def lgamma(x):
	return DuckDBOp(lambda x: 'lgamma' + '(' + f'{x}' + ')', x)

def ln(x):
	return DuckDBOp(lambda x: 'ln' + '(' + f'{x}' + ')', x)

def log(x):
	return DuckDBOp(lambda x: 'log' + '(' + f'{x}' + ')', x)

def log2(x):
	return DuckDBOp(lambda x: 'log2' + '(' + f'{x}' + ')', x)

def log10(x):
	return DuckDBOp(lambda x: 'log10' + '(' + f'{x}' + ')', x)

def nextafter(x, y):
	return DuckDBOp(lambda x, y: 'nextafter' + '(' + f'{x}, {y}' + ')', [x, y])

def pow(x, y):
	return DuckDBOp(lambda x, y: 'pow' + '(' + f'{x}, {y}' + ')', [x, y])

def power(x, y):
	return DuckDBOp(lambda x, y: 'power' + '(' + f'{x}, {y}' + ')', [x, y])

def radians(x):
	return DuckDBOp(lambda x: 'radians' + '(' + f'{x}' + ')', x)

def round(v, s):
	return DuckDBOp(lambda v, s: 'round' + '(' + f'{v}, {s}' + ')', [v, s])

def setseed(x):
	return DuckDBOp(lambda x: 'setseed' + '(' + f'{x}' + ')', x)

def sin(x):
	return DuckDBOp(lambda x: 'sin' + '(' + f'{x}' + ')', x)

def sign(x):
	return DuckDBOp(lambda x: 'sign' + '(' + f'{x}' + ')', x)

def signbit(x):
	return DuckDBOp(lambda x: 'signbit' + '(' + f'{x}' + ')', x)

def sqrt(x):
	return DuckDBOp(lambda x: 'sqrt' + '(' + f'{x}' + ')', x)

def xor(x):
	return DuckDBOp(lambda x: 'xor' + '(' + f'{x}' + ')', x)

def tan(x):
	return DuckDBOp(lambda x: 'tan' + '(' + f'{x}' + ')', x)

class FastPandas:
	def __init__(self, dataframe, graph=None, where=None):
		self.dataframe = dataframe
		self.graph = graph
		self.where = where

	def __getitem__(self, item):
		return self.column(item)

	def column(self, name):
		if name in self.dataframe.columns:
			return FastPandas(self.dataframe, DuckDBOp(lambda c: c, f'"{name}"'))
		else:
			raise KeyError(f"{name} not in columns")


	def filter(self, condition: "FastPandas"):
		return FastPandas(self.dataframe, self.graph, DuckDBOp(lambda x: x, condition))

	def item(self):
		_df = self.dataframe
		name = self.graph.compile()
		where_clause = ""
		if self.where is not None:
			where_clause = self.where.compile()

		query = f"SELECT {name} as result from _df"

		if where_clause != "":
			query += f" WHERE {where_clause}"

		return duckdb.query(query).df()["result"][0]

	def df(self):
		_df = self.dataframe
		name = self.graph.compile()
		where_clause = ""
		if self.where is not None:
			where_clause = self.where.compile()

		query = f"SELECT {name} from _df"

		if where_clause != "":
			query += f" WHERE {where_clause}"

		return duckdb.query(query).df()

	def __repr__(self) -> str:
		output = self.graph.compile()
		if self.where is not None:
			output += f" WHERE {self.where.compile()}"
		return output

	def add(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '+' + str(other) + ')', self.graph), self.where)

	def sub(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '-' + str(other) + ')', self.graph), self.where)

	def mul(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '*' + str(other) + ')', self.graph), self.where)

	def div(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '/' + str(other) + ')', self.graph), self.where)

	def mod(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '%' + str(other) + ')', self.graph), self.where)

	def lshift(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '<<' + str(other) + ')', self.graph), self.where)

	def rshift(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '>>' + str(other) + ')', self.graph), self.where)

	def gt(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '>' + str(other) + ')', self.graph), self.where)

	def gte(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '>=' + str(other) + ')', self.graph), self.where)

	def lt(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '<' + str(other) + ')', self.graph), self.where)

	def lte(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '<=' + str(other) + ')', self.graph), self.where)

	def eq(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '=' + str(other) + ')', self.graph), self.where)

	def neq(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '!=' + str(other) + ')', self.graph), self.where)

	def _and(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + 'and' + str(other) + ')', self.graph), self.where)

	def _or(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + 'or' + str(other) + ')', self.graph), self.where)

	def _is(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + 'is' + str(other) + ')', self.graph), self.where)

	def _is_not(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + 'is not' + str(other) + ')', self.graph), self.where)

	def bigint(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'BIGINT', self.graph), self.where)

	def int(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'INT', self.graph), self.where)

	def tinyint(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'TINYINT', self.graph), self.where)

	def hugeint(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'HUGEINT', self.graph), self.where)

	def smallint(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'SMALLINT', self.graph), self.where)

	def ubigint(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'UBIGINT', self.graph), self.where)

	def uint(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'UINTEGER', self.graph), self.where)

	def utinyint(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'UTINYINT', self.graph), self.where)

	def usmallint(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'USMALLINT', self.graph), self.where)

	def double(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'DOUBLE', self.graph), self.where)

	def bool(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'BOOLEAN', self.graph), self.where)

	def varchar(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'VARCHAR', self.graph), self.where)

	def date(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'DATE', self.graph), self.where)

	def timestamp(self):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + ')::' + 'TIMESTAMP', self.graph), self.where)

	def avg(self):
		return FastPandas(self.dataframe, avg(self.graph), self.where)

	def bit_and(self):
		return FastPandas(self.dataframe, bit_and(self.graph), self.where)

	def bit_or(self):
		return FastPandas(self.dataframe, bit_or(self.graph), self.where)

	def bit_xor(self):
		return FastPandas(self.dataframe, bit_xor(self.graph), self.where)

	def bool_and(self):
		return FastPandas(self.dataframe, bool_and(self.graph), self.where)

	def bool_or(self):
		return FastPandas(self.dataframe, bool_or(self.graph), self.where)

	def count(self):
		return FastPandas(self.dataframe, count(self.graph), self.where)

	def first(self):
		return FastPandas(self.dataframe, first(self.graph), self.where)

	def histogram(self):
		return FastPandas(self.dataframe, histogram(self.graph), self.where)

	def last(self):
		return FastPandas(self.dataframe, last(self.graph), self.where)

	def list(self):
		return FastPandas(self.dataframe, list(self.graph), self.where)

	def max(self):
		return FastPandas(self.dataframe, max(self.graph), self.where)

	def min(self):
		return FastPandas(self.dataframe, min(self.graph), self.where)

	def product(self):
		return FastPandas(self.dataframe, product(self.graph), self.where)

	def string_agg(self,sep):
		return FastPandas(self.dataframe, string_agg(self.graph,sep), self.where)

	def sum(self):
		return FastPandas(self.dataframe, sum(self.graph), self.where)

	def approx_count_distinct(self):
		return FastPandas(self.dataframe, approx_count_distinct(self.graph), self.where)

	def approx_quantile(self,pos):
		return FastPandas(self.dataframe, approx_quantile(self.graph,pos), self.where)

	def reservoir_quantile(self,quantile, sample_size):
		return FastPandas(self.dataframe, reservoir_quantile(self.graph,quantile, sample_size), self.where)

	def corr(self,x):
		return FastPandas(self.dataframe, corr(self.graph,x), self.where)

	def covar_pop(self,x):
		return FastPandas(self.dataframe, covar_pop(self.graph,x), self.where)

	def entropy(self):
		return FastPandas(self.dataframe, entropy(self.graph), self.where)

	def kurtosis(self):
		return FastPandas(self.dataframe, kurtosis(self.graph), self.where)

	def mode(self):
		return FastPandas(self.dataframe, mode(self.graph), self.where)

	def quantile_cont(self,pos):
		return FastPandas(self.dataframe, quantile_cont(self.graph,pos), self.where)

	def quantile_disc(self,pos):
		return FastPandas(self.dataframe, quantile_disc(self.graph,pos), self.where)

	def regr_avgx(self,x):
		return FastPandas(self.dataframe, regr_avgx(self.graph,x), self.where)

	def regr_avgy(self,x):
		return FastPandas(self.dataframe, regr_avgy(self.graph,x), self.where)

	def regr_count(self,x):
		return FastPandas(self.dataframe, regr_count(self.graph,x), self.where)

	def regr_intercept(self,x):
		return FastPandas(self.dataframe, regr_intercept(self.graph,x), self.where)

	def regr_r2(self,x):
		return FastPandas(self.dataframe, regr_r2(self.graph,x), self.where)

	def regr_slope(self,x):
		return FastPandas(self.dataframe, regr_slope(self.graph,x), self.where)

	def regr_sxx(self,x):
		return FastPandas(self.dataframe, regr_sxx(self.graph,x), self.where)

	def regr_sxy(self,x):
		return FastPandas(self.dataframe, regr_sxy(self.graph,x), self.where)

	def regr_syy(self,x):
		return FastPandas(self.dataframe, regr_syy(self.graph,x), self.where)

	def skewness(self):
		return FastPandas(self.dataframe, skewness(self.graph), self.where)

	def stddev_pop(self):
		return FastPandas(self.dataframe, stddev_pop(self.graph), self.where)

	def stddev_samp(self):
		return FastPandas(self.dataframe, stddev_samp(self.graph), self.where)

	def var_pop(self):
		return FastPandas(self.dataframe, var_pop(self.graph), self.where)

	def var_samp(self):
		return FastPandas(self.dataframe, var_samp(self.graph), self.where)

	def abs(self):
		return FastPandas(self.dataframe, abs(self.graph), self.where)

	def acos(self):
		return FastPandas(self.dataframe, acos(self.graph), self.where)

	def asin(self):
		return FastPandas(self.dataframe, asin(self.graph), self.where)

	def atan(self):
		return FastPandas(self.dataframe, atan(self.graph), self.where)

	def atan2(self,y):
		return FastPandas(self.dataframe, atan2(self.graph,y), self.where)

	def bit_count(self):
		return FastPandas(self.dataframe, bit_count(self.graph), self.where)

	def cbrt(self):
		return FastPandas(self.dataframe, cbrt(self.graph), self.where)

	def ceil(self):
		return FastPandas(self.dataframe, ceil(self.graph), self.where)

	def ceiling(self):
		return FastPandas(self.dataframe, ceiling(self.graph), self.where)

	def cos(self):
		return FastPandas(self.dataframe, cos(self.graph), self.where)

	def cot(self):
		return FastPandas(self.dataframe, cot(self.graph), self.where)

	def degrees(self):
		return FastPandas(self.dataframe, degrees(self.graph), self.where)

	def even(self):
		return FastPandas(self.dataframe, even(self.graph), self.where)

	def factorial(self):
		return FastPandas(self.dataframe, factorial(self.graph), self.where)

	def floor(self):
		return FastPandas(self.dataframe, floor(self.graph), self.where)

	def gamma(self):
		return FastPandas(self.dataframe, gamma(self.graph), self.where)

	def gcd(self,y):
		return FastPandas(self.dataframe, gcd(self.graph,y), self.where)

	def greatest_common_divisor(self,y):
		return FastPandas(self.dataframe, greatest_common_divisor(self.graph,y), self.where)

	def isfinite(self):
		return FastPandas(self.dataframe, isfinite(self.graph), self.where)

	def isinf(self):
		return FastPandas(self.dataframe, isinf(self.graph), self.where)

	def isnan(self):
		return FastPandas(self.dataframe, isnan(self.graph), self.where)

	def lcm(self,y):
		return FastPandas(self.dataframe, lcm(self.graph,y), self.where)

	def least_common_multiple(self,y):
		return FastPandas(self.dataframe, least_common_multiple(self.graph,y), self.where)

	def lgamma(self):
		return FastPandas(self.dataframe, lgamma(self.graph), self.where)

	def ln(self):
		return FastPandas(self.dataframe, ln(self.graph), self.where)

	def log(self):
		return FastPandas(self.dataframe, log(self.graph), self.where)

	def log2(self):
		return FastPandas(self.dataframe, log2(self.graph), self.where)

	def log10(self):
		return FastPandas(self.dataframe, log10(self.graph), self.where)

	def nextafter(self,y):
		return FastPandas(self.dataframe, nextafter(self.graph,y), self.where)

	def pow(self,y):
		return FastPandas(self.dataframe, pow(self.graph,y), self.where)

	def power(self,y):
		return FastPandas(self.dataframe, power(self.graph,y), self.where)

	def radians(self):
		return FastPandas(self.dataframe, radians(self.graph), self.where)

	def round(self,s):
		return FastPandas(self.dataframe, round(self.graph,s), self.where)

	def setseed(self):
		return FastPandas(self.dataframe, setseed(self.graph), self.where)

	def sin(self):
		return FastPandas(self.dataframe, sin(self.graph), self.where)

	def sign(self):
		return FastPandas(self.dataframe, sign(self.graph), self.where)

	def signbit(self):
		return FastPandas(self.dataframe, signbit(self.graph), self.where)

	def sqrt(self):
		return FastPandas(self.dataframe, sqrt(self.graph), self.where)

	def xor(self):
		return FastPandas(self.dataframe, xor(self.graph), self.where)

	def tan(self):
		return FastPandas(self.dataframe, tan(self.graph), self.where)

