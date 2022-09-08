class Chromosome:

	def __init__(self, name, start, end, cent):
		self.name = name
		self.start = start
		self.end = end	
		self.cent = cent

	def addCent(self, newCent):
		self.cent = newCent