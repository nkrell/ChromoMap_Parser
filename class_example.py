@total_ordering #this method forces the class to determine ordering based on just the overriden le, gt methods
class Dog:

	def __init__(self, breed furColor, name, age = 0):
		self.furColor = furColor
		self.breed = breed
		self.name = name
		self.age = age
	def bark(self):
		print(name + " barks")

	#overriding
	#str is for string conversion
	def __str__(self):
		return self.name
	#formal converson, used for checking values when debugging
	def __repr__(self):
	# set boolean logic when comparing objecs of Dog class
	def __eq__(self, other):


		
class DogPark:
	#*args makes an unlimited potential number of arguments, such that any number of dogs could be put in the park
	def __init__(self, *args):
		self.dogsInPark = []
		for dog in args:
			self.dogsInPark.append(dog)
	#must override these two to make dogpark iterable
	self.i = 0
	def __iter__(self):
		yeild from self.dogsInPark #this works cause its already a list
	# 	return self
	# def __next__(self):
	# 	val = i
	# 	self.i += 1
	# 	if val < len(self.dogsInPark):
	# 		return self.dogsInPark[val]
	# 	else:
	# 		raise StopIteration
def main():

	d = dog("corgi", "tricolor", "po")
	d.bark()
	d. dog(furColor="brown", name= "bruh", breed= "dog")