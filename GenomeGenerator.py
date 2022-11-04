import os
import random

def main():
	for i in range(0, 10):
		newFile = open("A_real_genome_" + str(i) +"_.fna", "w")
		for j in range(0, 22):
			newFile.write(randomHeader(i))
			newFile.write("\n")
			for k in range(0,50000000):
				newFile.write(randomCodon())
		
		#newFile.write(randomChromosome())
		newFile.write("\n")
		print("Done")

def randomHeader(iterationNum):
	print("Writing: ")
	print(">A_real_chromosome_I_Swear_" + str(iterationNum))
	return(">A_real_chromosome_I_Swear_" + str(iterationNum))	


#def randomChromosome():
#	chromosome = ""
#	for i in range(0,10000000):
#		chromosome += randomCodon()
#	return(chromosome)

def randomCodon():
	codon = ""
	for i in range(0,3):
		codon += randomBase()
	return(codon)

def randomBase():
	base = ""
	choice = random.randint(1,4)
	if choice == 1:
		base = "A"
	elif choice == 2:
		base = "T"
	elif choice == 3:
		base = "C"
	else:
		base = "G"
	return(base)

if __name__ == '__main__':
	main()