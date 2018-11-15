class Circle():

	pi = 3.14
	def __init__(self,radius):
		self.radius = radius
	#method
	def get_circum(self):
		return self.radius*Circle.pi*2
my_circle = Circle(3)
print(my_circle.get_circum())


