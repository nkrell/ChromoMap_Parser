from Chr_Class import Chromosome as Chromosome
from Genome_Class import Genome as Genome
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
	#list for holding genome objects
	genomeList = list()
	#variable for holding length of chromosome
	chrLength = 0
	#variable for holding genome name
	genomeName = ""
	#lists for holding chr data
	headerList = list()
	lengthList = list()
	#flag for traking line type
	isHeader = True
	for file in os.listdir():
		if file.endswith(".fna"):
			#get name of genome
			genomeName = file
			#list to hold chromosome objects
			chrList = list()
			with open(file) as fh:
				for line in fh:
					if line.startswith(">"):
						#trim header to assention number
						line = line.split(" ")
						line = line[0]
						headerList.append(line.strip("\n"))
						if chrLength != 0:
							lengthList.append(chrLength)
							chrLength = 0
					else:
						chrLength += len(line.strip("\n"))
					#add last chrLength as there are no more ">"
			lengthList.append(chrLength)
			#combine lists into a single data structure
			for i in range(0, len(headerList)):
				chrList.append(Chromosome(headerList[i], 1, lengthList[i], 0))
			genomeList.append(Genome(genomeName, chrList))

	for genome in genomeList:
		print(genome)
		print(len(genome.chrList))
		#for chrm in genome.chrList:
			#print(chrm)
	
	for genome in genomeList:
		newFile = open(genome.name() + ".chromosome", "w")
		for chrm in genome.chrList:
			newFile.write(chrm.writeLine())

		newFile.close()






if __name__ == '__main__':
	main()