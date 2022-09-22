import os

def main():
	#get folder name
	while True:
		try:
			print("Enter name of folder containing genomes for header parsing: ")
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

	
	for file in os.listdir():
		if file.endswith(".fna"):
			newFile = open(file + ".headers", "w")
			print("Parsing: " + file)
			with open(file) as fh:
				for line in fh:
					if line.startswith(">"):
						newFile.write(line)
			newFile.close()
			print("Done.")

if __name__ == '__main__':
	main()