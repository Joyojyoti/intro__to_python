#Like other oop languages python can also import other files and packages.
#Here function1 is imported as the name 'fu' and all functions in the file can be accessed by fu.function_name
import function1 as fu
data1 = fu.population_density(100,20)
data2 = fu.population_density(1000,300)
print(data1)
print(data2)


#by this method we can import only specified funtions or we can import all functions of a file by using '*'
#another helpful part is we don't have to write the file name again and again, rather we use the function by function_name directly.
from function1 import *
data3 = population_density(1000,20)
print(data3)