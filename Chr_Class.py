class Chromosome:

	def __init__(self, name, start, end, cent):
		self.name = name
		self.start = start
		self.end = end	
		self.cent = None

	def addCent(self, newCent):
		self.cent = newCent