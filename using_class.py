#Defining a class of name 'Student'
class Student:
#defining the properties that the class will contain
	def __init__(self, name, roll):
		self.name = name
		self.roll = roll
#defining the methods or functions of the class.
	def get_details(self):
		print("The Roll number of {} is {}.".format(self.name, self.roll))

#Creating the instance of class Student
stdnt1 = Student('Alexa',1234)
stdnt2 = Student('Joy',1235)
#Here Calling the functions of the class
stdnt2.get_details()
stdnt1.get_details()

"""The output will be like:
The Roll number of Joy is 1235.
The Roll number of Alexa is 1234. """