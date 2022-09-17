import os

def main():
	#get folder name
	while True:
		try:
			print("Enter name of folder containing genomes for parsing: ")
			targetFolder = input()
			if targetFolder not in os.listdir():
				raise ValueError
			else:
				pass
		except ValueError:
			print("Folder not found.")
		except FileNotFoundError:
			print("Folder not found.")
		else:
			break
	#navigate into target folder
	os.chdir(targetFolder)

	#read in each genome
	for file in os.listdir():
		if file.endswith(".fna"):
			readInGenome(file)

def readInGenome(filename):
	#declare required temporary variables
	chrLength = 0
	chrName = ""
	#create Genome object
	currentGenome = Genome(filename)
	#open file
	with open(filename) as fh:
		for line in fh:
			if line.startswith(">"):
						#trim header to assention number
						line = line.split(" ")
						line = line[0]
						chrName = line
						if chrLength != 0:
							#lengthList.append(chrLength)
							#create chromosome object for parsed chromosome data
							currentChromosome = Chromosome(chrName, 1, chrLength, 0)
							#add chromosome object to currentGenome
							currentGenome.addChromosome(currentChromosome)
							chrLength = 0
			else:
				chrLength += len(line.strip("\n"))
		#add last chromosome as there are no more ">"
		#lengthList.append(chrLength)
		#create chromosome object for parsed chromosome data
		currentChromosome = Chromosome(chrName, 1, chrLength, 0)
		#add chromosome object to currentGenome
		currentGenome.addChromosome(currentChromosome)

	#testing
	print(currentGenome)
	





###############################CLASSES#################################
class Genome:
	def __init__(self, genomeName):
		#initilize only the name with a value, the list will be filled via method later
		self.genomeName = genomeName
		self.chrList = list()

	def addChromosome(self, chromosome):
		#add new chromosome to list of chromosomes
		self.chrList.append(chromosome)

	def __str__(self):
		print(self.genomeName)
		for chromosome in self.chrList:
			print(chromosome)
		return(str(len(self.chrList)))

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


if __name__ == '__main__':
	main()