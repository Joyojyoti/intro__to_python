"""By this method file handling is done in Python. open('file_name with path specified','opening_mode') helps to open the file in 'read'
or 'write' mode """
f = open("another.txt","w")
# Then in write mode file can be written, some strings can be added
f.write("Hello People")
f.close()

f = open("another.txt","r")
# .read() command helps to read the string existing in the following file
file_data = f.read()
print(file_data)
# Closing of a file is necessary because if multiple files are opened in the code, 
# then to reduce complexity it ia a good practice to close the file if the following task is done.
f.close()

""" This is a new syntax of Python to open and access the file in one line of code,
and the most helpful part is, you don't have to close the file, once accessed, it will be automatically closed"""
with open("another.txt","r") as f:
	new_data = f.read()

print(new_data)