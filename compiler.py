# todo take into account functions with more than one parameter
unary_aggregates = [
    "avg(arg)",
    "bit_and(arg)",
    "bit_or(arg)",
    "bit_xor(arg)",
    "bool_and(arg)",
    "bool_or(arg)",
    "count(arg)",
    "first(arg)",
    "histogram(arg)",
    "last(arg)",
    "list(arg)",
    "max(arg)",
    "min(arg)",
    "product(arg)",
    # "string_agg(arg, sep)",
    "sum(arg)",
    "approx_count_distinct(x)",
    # "approx_quantile(x,pos)",
    # "reservoir_quantile(x,quantile,sample_size=8192)",
    # "corr(y,x)",
    # "covar_pop(y,x)",
    "entropy(x)",
    "kurtosis(x)",
    "mode(x)",
    # "quantile_cont(x,pos)",
    # "quantile_disc(x,pos)",
    # "regr_avgx(y,x)",
    # "regr_avgy(y,x)",
    # "regr_count(y,x)",
    # "regr_intercept(y,x)",
    # "regr_r2(y,x)",
    # "regr_slope(y,x)",
    # "regr_sxx(y,x)",
    # "regr_sxy(y,x)",
    # "regr_syy(y,x)",
    "skewness(x)",
    "stddev_pop(x)",
    "stddev_samp(x)",
    "var_pop(x)",
    "var_samp(x)",
]

unary_numerical = [
    "abs(x)",
    "acos(x)",
    # "atan2(x, y)",
    "bit_count(x)",
    "cbrt(x)",
    "ceil(x)",
    "chr(x)",
    "cos(x)",
    "cot(x)",
    "degrees(x)",
    "floor(x)",
    "ln(x)",
    "log(x)",
    "log2(x)",
    "pi()",
    # "pow(x, y)",
    "radians(x)",
    # "random()",
    # "round(v numeric, s int)",
    # "setseed(x)",
    "sin(x)",
    "sign(x)",
    "sqrt(x)",
    "tan(x)",
]

numerical_ops = [
    ("+", "add"),
    ("-", "sub"),
    ("*", "mul"),
    ("/", "div"),
    ("%", "mod"),
    ("<<", "lshift"),
    (">>", "rshift"),
    ("&", "_and"),
    ("|", "_or"),
    ("#", "xor"),
]


unary = [*unary_aggregates, *unary_numerical]


def decompose_unary(u):
    name = u.split("(")[0]
    parameter = u.split("(")[1].split(")")[0]
    return name, parameter


def compile_unary(u):
    name, parameters = decompose_unary(u)
    func_name = "def {}:\n".format(u)
    func_body = "\treturn DuckDBUnary(lambda c: '{}' + '(' + c + ')', {})\n".format(
        name, parameters
    )
    full = func_name + func_body
    return full


def add_unary_to_class(u):
    name, _ = decompose_unary(u)
    func_name = "\tdef {}(self):\n".format(name)
    func_body = f"\t\treturn FastPandas(self.dataframe, {name}(self.graph))"
    full = func_name + func_body
    return full


def compile_numeric_operator(operator, nickname):
    func_name = f"\tdef {nickname}(self, other):\n"
    func_body = "\t\treturn FastPandas(self.dataframe, DuckDBUnary(lambda c: '(' + c + '{}' + str(other) + ')', self.graph))\n".format(
        operator
    )
    full = func_name + func_body
    return full


with open("fast_pandas.py", "w") as f:
    f.write("from lazy import DuckDBUnary\n\n")

    for u in unary:
        f.write(compile_unary(u) + "\n")

    fast_pandas_class = """class FastPandas:
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
		return self.graph.compile()\n
"""

    f.write(fast_pandas_class)

    for op, nickname in numerical_ops:
        f.write(compile_numeric_operator(op, nickname) + "\n")

    for u in unary:
        f.write(add_unary_to_class(u) + "\n\n")
