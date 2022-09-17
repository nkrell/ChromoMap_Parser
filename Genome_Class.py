#rom Chr_Class import Chromosome as Chromosome
class Genome:

	def __init__(self, genomeName, chrList):
		self.genomeName = genomeName
		self.chrList = chrList

	def __str__(self):
		return(self.genomeName + "\n")
		
	def name(self):
		return(self.genomeName)

	def printList(self):
		print(len(self.chrList))
		for chrm in self.chrList:
			print(chrm.writeLine())



	