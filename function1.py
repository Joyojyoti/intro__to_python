# By this Procedure functions aree defined in Python
# It returns value by 'return' statement
def population_density(population,land_area):
	return population/land_area

# This chunk of code is executed when only this file executed as main file
# If any other file is importing this file then the below codes will not execute in that file
# We have imported this file in an another file, named 'importing_function1.py'
if __name__ == '__main__':
		return_value=population_density(20,10)
		print(return_value)

