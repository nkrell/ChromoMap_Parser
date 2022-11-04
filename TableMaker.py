import os

def main():
	#get folder name
	while True:
		try:
			print("Enter name files for tabulation: ")
			targetFile = input()
			targetFile = targetFile + ".txt"
			if targetFile not in os.listdir():
				raise ValueError
			else:
				pass
		except ValueError:
			print("File not found.")
		except FileNotFoundError:
			print("File not found.")
		else:
			break
	#read in headers of main file
	headerList = readInHeaders(targetFile)
	#remove .txt from targetFile
	targetFile = targetFile.strip(".txt")



def readInHeaders(targetFile):
	headerList = list()
	isFirstLine = True
	with open(targetFile) as fh:
		for line in fh:
			if isFirstLine = True:
				line = line.split(",")
				for head in line:
					headerList.append(head)
			isFirstLine = False
	return(headerList)

def readInTables(targetFile, headerList):
	codingList = list()
	psuedoList = list()
	#will be used, reset, and then used again
	positionList = list()

	with open(targetFile + "_coding_status.txt")




	