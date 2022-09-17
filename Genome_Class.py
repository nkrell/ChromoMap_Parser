class Genome:

	def __init__(self, genomeName, chrList):
		self.genomeName = genomeName
		self.chrList = chrList

	def __str__(self):
		return(self.genomeName + "\n")
		
	def name(self):
		return(self.genomeName)

	