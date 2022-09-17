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





###############################CLASSES#################################
class Genome:
	def __init__(self, genomeName):
		#initilize only the name witha value, the list will be filled via method later
		self.genomeName = genomeName
		self.chrList = list()

	def fillChrList()


if __name__ == '__main__':
	main()