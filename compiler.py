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
    "string_agg(arg, sep)",
    "sum(arg)",
    "approx_count_distinct(x)",
    "approx_quantile(x,pos)",
    # todo account for default args (sample_size is default here)
    "reservoir_quantile(x,quantile,sample_size)",
    "corr(y,x)",
    "covar_pop(y,x)",
    "entropy(x)",
    "kurtosis(x)",
    "mode(x)",
    "quantile_cont(x,pos)",
    "quantile_disc(x,pos)",
    "regr_avgx(y,x)",
    "regr_avgy(y,x)",
    "regr_count(y,x)",
    "regr_intercept(y,x)",
    "regr_r2(y,x)",
    "regr_slope(y,x)",
    "regr_sxx(y,x)",
    "regr_sxy(y,x)",
    "regr_syy(y,x)",
    "skewness(x)",
    "stddev_pop(x)",
    "stddev_samp(x)",
    "var_pop(x)",
    "var_samp(x)",
]

# todo account for constants ie pi()
unary_numerical = [
    "abs(x)",
    "acos(x)",
    "atan2(x, y)",
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
    # "pi()",
    "pow(x, y)",
    "radians(x)",
    # "random()",
    "round(v, s)",
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
]

where_ops = [
    (">", "gt"),
    (">=", "gte"),
    ("<", "lt"),
    ("<=", "lte"),
    ("=", "eq"),
    ("!=", "neq"),
]

where_connectives = [
    ("and", "_and"),
    ("or", "_or"),
    ("is", "_is"),
    ("is not", "_is_not"),
]


unary = [*unary_aggregates, *unary_numerical]


def parse_func(u="pow(x, y, z)"):
    # outputs = ('pow', ['x', 'y', 'z'])
    name = u.split("(")[0]
    parameters = u.split("(")[1].split(")")[0].split(",")
    return name, [parameters.strip() for parameters in parameters]


def str_params(list_of_params, brackets=False):
    if len(list_of_params) == 1:
        return str(list_of_params[0])

    output = ", ".join([str(param) for param in list_of_params])
    if brackets:
        output = "[" + output + "]"

    return output


def str_params_with_brackets(list_of_params):
    return ", ".join(["{" + str(param) + "}" for param in list_of_params])


def f_str_params(list_of_params):
    # given x, y, z
    # return f'{x}, {y}, {z}'
    return "f'" + str_params_with_brackets(list_of_params) + "'"


def compile_unary(u):
    name, parameters = parse_func(u)
    func_name = "def {}:\n".format(u)
    _str_params = str_params(parameters)
    func_body = "\treturn DuckDBOp(lambda {}: '{}' + '(' + {} + ')', {})\n".format(
        _str_params, name, f_str_params(parameters), str_params(parameters, True)
    )
    full = func_name + func_body
    return full


def add_unary_to_class(u):
    name, parameters = parse_func(u)
    _str_params = "," + str_params(parameters[1:]) if len(parameters) > 1 else ""
    func_name = "\tdef {}(self{}):\n".format(name, _str_params)
    # what if the param is not a primitive? what if its another column?
    func_body = (
        f"\t\treturn FastPandas(self.dataframe, {name}(self.graph{_str_params}), self.where)"
    )
    full = func_name + func_body
    return full


def compile_numeric_operator(operator, nickname):
    func_name = f"\tdef {nickname}(self, other):\n"
    func_body = "\t\treturn FastPandas(self.dataframe, DuckDBOp(lambda c: '(' + c + '{}' + str(other) + ')', self.graph), self.where)\n".format(
        operator
    )
    full = func_name + func_body
    return full


def compile_where(operator, nickname):
    return compile_numeric_operator(operator, nickname)


def compile_where_connectives(operator, nickname):
    return compile_numeric_operator(operator, nickname)


def compile_all():
    with open("fast_pandas.py", "w") as f:
        f.write("import duckdb\n")
        f.write("from lazy import DuckDBOp\n\n")

        for u in unary:
            f.write(compile_unary(u) + "\n")

        fast_pandas_class = """class FastPandas:
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
		return output\n\n"""

        f.write(fast_pandas_class)

        for op, nickname in numerical_ops:
            f.write(compile_numeric_operator(op, nickname) + "\n")

        for op, nickname in where_ops:
            f.write(compile_where(op, nickname) + "\n")

        for op, nickname in where_connectives:
            f.write(compile_where_connectives(op, nickname) + "\n")

        for u in unary:
            f.write(add_unary_to_class(u) + "\n\n")


compile_all()
