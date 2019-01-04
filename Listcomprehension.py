""" List comprehension is the smaller version of a loop in Python,
using this type of syntax you can access for and while loop with if-else condition in just one line of code"""
names=['name1','name2','name3','name4','name5']
lowername = [name.replace("name4","another_name").title() for name in names]
print(lowername)
#this will print the list as title format using .title() function and 
#.replace() function helps to replace some particular part of the list of srting 


#again this is a list comprehension where cube of 1 to 20 is being printed
mul_3 = [x**3 for x in range(1,21)]
print(mul_3)