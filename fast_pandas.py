from lazy import DuckDBOp

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

def atan2(x, y):
	return DuckDBOp(lambda x, y: 'atan2' + '(' + f'{x}, {y}' + ')', [x, y])

def bit_count(x):
	return DuckDBOp(lambda x: 'bit_count' + '(' + f'{x}' + ')', x)

def cbrt(x):
	return DuckDBOp(lambda x: 'cbrt' + '(' + f'{x}' + ')', x)

def ceil(x):
	return DuckDBOp(lambda x: 'ceil' + '(' + f'{x}' + ')', x)

def chr(x):
	return DuckDBOp(lambda x: 'chr' + '(' + f'{x}' + ')', x)

def cos(x):
	return DuckDBOp(lambda x: 'cos' + '(' + f'{x}' + ')', x)

def cot(x):
	return DuckDBOp(lambda x: 'cot' + '(' + f'{x}' + ')', x)

def degrees(x):
	return DuckDBOp(lambda x: 'degrees' + '(' + f'{x}' + ')', x)

def floor(x):
	return DuckDBOp(lambda x: 'floor' + '(' + f'{x}' + ')', x)

def ln(x):
	return DuckDBOp(lambda x: 'ln' + '(' + f'{x}' + ')', x)

def log(x):
	return DuckDBOp(lambda x: 'log' + '(' + f'{x}' + ')', x)

def log2(x):
	return DuckDBOp(lambda x: 'log2' + '(' + f'{x}' + ')', x)

def pow(x, y):
	return DuckDBOp(lambda x, y: 'pow' + '(' + f'{x}, {y}' + ')', [x, y])

def radians(x):
	return DuckDBOp(lambda x: 'radians' + '(' + f'{x}' + ')', x)

def round(v, s):
	return DuckDBOp(lambda v, s: 'round' + '(' + f'{v}, {s}' + ')', [v, s])

def sin(x):
	return DuckDBOp(lambda x: 'sin' + '(' + f'{x}' + ')', x)

def sign(x):
	return DuckDBOp(lambda x: 'sign' + '(' + f'{x}' + ')', x)

def sqrt(x):
	return DuckDBOp(lambda x: 'sqrt' + '(' + f'{x}' + ')', x)

def tan(x):
	return DuckDBOp(lambda x: 'tan' + '(' + f'{x}' + ')', x)

class FastPandas:
	def __init__(self, dataframe, graph=None):
		self.dataframe = dataframe
		self.graph = graph

	def __getitem__(self, item):
		return self.column(item)

	def column(self, name):
		if name in self.dataframe.columns:
			return FastPandas(self.dataframe, DuckDBOp(lambda c: c, f'"{name}"'))
		else:
			raise KeyError(f"{name} not in columns")

	def df(self):
		return self.graph.df(self.dataframe)

	def item(self):
		return self.graph.item(self.dataframe)

	def __repr__(self) -> str:
		return self.graph.compile()

	def add(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '+' + str(other) + ')', self.graph))

	def sub(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '-' + str(other) + ')', self.graph))

	def mul(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '*' + str(other) + ')', self.graph))

	def div(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '/' + str(other) + ')', self.graph))

	def mod(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '%' + str(other) + ')', self.graph))

	def lshift(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '<<' + str(other) + ')', self.graph))

	def rshift(self, other):
		return FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '>>' + str(other) + ')', self.graph))

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

	def string_agg(self,sep):
		return FastPandas(self.dataframe, string_agg(self.graph,sep))

	def sum(self):
		return FastPandas(self.dataframe, sum(self.graph))

	def approx_count_distinct(self):
		return FastPandas(self.dataframe, approx_count_distinct(self.graph))

	def approx_quantile(self,pos):
		return FastPandas(self.dataframe, approx_quantile(self.graph,pos))

	def reservoir_quantile(self,quantile, sample_size):
		return FastPandas(self.dataframe, reservoir_quantile(self.graph,quantile, sample_size))

	def corr(self,x):
		return FastPandas(self.dataframe, corr(self.graph,x))

	def covar_pop(self,x):
		return FastPandas(self.dataframe, covar_pop(self.graph,x))

	def entropy(self):
		return FastPandas(self.dataframe, entropy(self.graph))

	def kurtosis(self):
		return FastPandas(self.dataframe, kurtosis(self.graph))

	def mode(self):
		return FastPandas(self.dataframe, mode(self.graph))

	def quantile_cont(self,pos):
		return FastPandas(self.dataframe, quantile_cont(self.graph,pos))

	def quantile_disc(self,pos):
		return FastPandas(self.dataframe, quantile_disc(self.graph,pos))

	def regr_avgx(self,x):
		return FastPandas(self.dataframe, regr_avgx(self.graph,x))

	def regr_avgy(self,x):
		return FastPandas(self.dataframe, regr_avgy(self.graph,x))

	def regr_count(self,x):
		return FastPandas(self.dataframe, regr_count(self.graph,x))

	def regr_intercept(self,x):
		return FastPandas(self.dataframe, regr_intercept(self.graph,x))

	def regr_r2(self,x):
		return FastPandas(self.dataframe, regr_r2(self.graph,x))

	def regr_slope(self,x):
		return FastPandas(self.dataframe, regr_slope(self.graph,x))

	def regr_sxx(self,x):
		return FastPandas(self.dataframe, regr_sxx(self.graph,x))

	def regr_sxy(self,x):
		return FastPandas(self.dataframe, regr_sxy(self.graph,x))

	def regr_syy(self,x):
		return FastPandas(self.dataframe, regr_syy(self.graph,x))

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

	def atan2(self,y):
		return FastPandas(self.dataframe, atan2(self.graph,y))

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

	def pow(self,y):
		return FastPandas(self.dataframe, pow(self.graph,y))

	def radians(self):
		return FastPandas(self.dataframe, radians(self.graph))

	def round(self,s):
		return FastPandas(self.dataframe, round(self.graph,s))

	def sin(self):
		return FastPandas(self.dataframe, sin(self.graph))

	def sign(self):
		return FastPandas(self.dataframe, sign(self.graph))

	def sqrt(self):
		return FastPandas(self.dataframe, sqrt(self.graph))

	def tan(self):
		return FastPandas(self.dataframe, tan(self.graph))

