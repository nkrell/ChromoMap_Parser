#from Genome_Class import Genome as Genome
class Chromosome:

	def __init__(self, name, start, end, cent):
		self.name = name
		self.start = start
		self.end = end	
		self.cent = cent

	def addCent(self, newCent):
		self.cent = newCent

	def __str__(self):
		return(self.name + "\t" + str(self.start) + "\t" + str(self.end) + "\n")

	def chrName(self):
		return(self.name)

	def start(self):
		return(self.start)

	def end(self):
		return(self.end)

	def writeLine(self):
		return(self.name + "\t" + str(self.start) + "\t" + str(self.end) + "\n")