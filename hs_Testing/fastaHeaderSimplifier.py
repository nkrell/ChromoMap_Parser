import os

def main():
	#delcare required variables
	geneType = ""
	codingStatus = ""
	#for all the files in the current directory
	for file in os.listdir():
		#if the file is of the correct type
		if file.endswith(".clean.fasta"):
			#open new file so it can be wrtten line-for-line as the old file is parsed
			newFile = open(file + ".simple_headers", "w")
			#open file
			with open(file) as fh:
				#for each line in the file
				for line in fh:
					#if the line is a header
					if line.startswith(">"):
						#remove the end-line symbol from the end 
						line = line.strip("\n")
						#split line by "|" symbols
						line = line.split("|")
						#check if it was a pseudogene
						if len(line) == 2:
							geneType = line[1]
							codingStatus = "CODING"
						elif len(line) == 3:
							geneType = line[1]
							codingStatus = line[2]
						#write the header to the new file
						newFile.write(">")
						newFile.write(geneType + "_" + codingStatus)
						newFile.write("\n")
					#if the line is part of a sequence
					elif not line.startswith(">"):
						#write sequence line to new file
						newFile.write(line)
			#close new file 
			newFile.close()



if __name__ == '__main__':
	main()