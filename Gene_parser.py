import os

def main():
	#get folder name
	while True:
		try:
			print("Enter name of folder containing genes for parsing: ")
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

	#for all file in the folder
	for file in os.listdir():
		#if the file type is correct
		if file.endswith(".gff3"):
			#call readInGenes method
			geneList = readInGenes(file)
			#write out new file
			newFile = open(file + ".genes", "w")
			for gene in geneList:
				newFile.write(gene.writeGene())
				newFile.write("\n")
			newFile.close()
		
		


def readInGenes(filename):
	#delcare required variables
	geneList = list()
	currentGene = None
	chromosomeName = ""
	geneName = ""
	geneStart = ""
	geneEnd = ""
	geneData = ""
	with open(filename) as fh:
		for line in fh:
			#split line by tabs
			line = line.split("\t")
			#move data into temporary varaiables to make code more readable
			chromosomeName = line[0]
			geneName = line[8]
			geneStart = line[3]
			geneEnd = line[4]
			#trim data from line 8
			geneName = geneName.split("=")
			geneName = geneName[2]
			geneName = geneName.split("_")
			#determine whether its coding or not
			if "CODING" in geneName[1]:
				geneData = "CODING"
			elif "PSEUDOGENE" in geneName[1]:
				geneData = "PSEUDOGENE"
			#finish parsing geneName
			geneName = geneName[0]
			#move parsed data into gene object
			currentGene = Gene(geneName, chromosomeName, geneStart, geneEnd, geneData)
			#add each gene to geneList once each line has been parsed
			geneList.append(currentGene)
	#return a list of gene objects made using hte parsed information
	return(geneList)



########################################CLASSES############################################
class Gene:

	
	

	def __init__(self, geneName, chromosomeName, geneStart, geneEnd, geneData):
		self.geneName = geneName
		self.chromosomeName = chromosomeName
		self.geneStart = geneStart
		self.geneEnd = geneEnd
		self.geneData = geneData

	def __str__(self):
		#an internal class variable to i dont have to type "\t"
		tab = "\t"
		return(self.geneName + tab + self.chromosomeName + tab + self.geneStart + tab + self.geneEnd + tab + self.geneData)

	def writeGene(self):
		#an internal class variable to i dont have to type "\t"
		tab = "\t"
		return(self.geneName + tab + self.chromosomeName + tab + self.geneStart + tab + self.geneEnd + tab + self.geneData)























if __name__ == '__main__':
	main()