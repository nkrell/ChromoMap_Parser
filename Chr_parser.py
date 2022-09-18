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
		#define a genome object to exist within the scope of this loop
		#the genome object is used to hold the readInGenome() output, and then it is used as input for the writeing method
		#then it falls out of scope
		#this way memeory can be conserved
		if file.endswith(".fna"):
			print("Reading file: " + file)
			currentGenome = readInGenome(file)
			print("Reading file: " + file + ".chrmap")
			currentGenome.writeFile()


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
						line = line.lstrip(">")
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
	return(currentGenome)






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
		# <------------------------------Update this so it isnt so stupid <----------------------------------------------
		print(self.genomeName)
		for chromosome in self.chrList:
			print(chromosome)
		return(str(len(self.chrList)))

	#class method for returning genome name when writing files
	def getName(self):
		return(self.genomeName)

	#class method for retruning chrList when writing files
	def getChrList(self):
		return(self.chrList)

	#self contained file-writing method
	def writeFile(self):
		newFile = open(self.genomeName + ".chrmap", "w")
		for chromosome in self.chrList:
			newFile.write(chromosome.chrName() + "\t" + str(chromosome.chrStart()) + "\t" + str(chromosome.chrEnd()))
			newFile.write("\n")
		newFile.close()

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

	def chrStart(self):
		return(self.start)

	def chrEnd(self):
		return(self.end)

	def writeLine(self):
		return(self.name + "\t" + str(self.start) + "\t" + str(self.end) + "\n")



if __name__ == '__main__':
	main()