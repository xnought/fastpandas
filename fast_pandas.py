from lazy import DuckDBUnary


def entropy(x):
	return DuckDBUnary(lambda c: 'entropy' + '(' + c + ')', x)


def approx_count_distinct(x):
	return DuckDBUnary(lambda c: 'approx_count_distinct' + '(' + c + ')', x)


def abs(x):
	return DuckDBUnary(lambda c: 'abs' + '(' + c + ')', x)

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

	def entropy(self):
		return FastPandas(self.dataframe, entropy(self.graph))

	def approx_count_distinct(self):
		return FastPandas(self.dataframe, approx_count_distinct(self.graph))

	def abs(self):
		return FastPandas(self.dataframe, abs(self.graph))

