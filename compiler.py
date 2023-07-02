unary = ["entropy(x)", "approx_count_distinct(x)", "abs(x)"]


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


with open("fast_pandas.py", "w") as f:
    f.write("from lazy import DuckDBUnary\n\n")

    for u in unary:
        f.write("\n" + compile_unary(u) + "\n")

    f.write(
        """class FastPandas:
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
    )

    for u in unary:
        f.write(add_unary_to_class(u) + "\n\n")
