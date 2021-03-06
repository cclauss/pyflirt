class _map:
	def __init__(self, functions, path):
		self.file = open(path, "w")
		self.write_function(functions)
		self.file.close()

	def write_function(self, functions):
		self.file.write("\n\n  Address         Publics by Value\n")
		for address in sorted(functions):
			#only print fucntions with name
			if len(functions[address]) > 1:
				# section:address       name
				self.file.write("\n %04X:%08X       %s" % (functions[address][0] + 1, address, functions[address][1]))