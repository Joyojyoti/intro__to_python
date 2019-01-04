# When try statement gets into any error the block of code in the except statement will get executed
try:
	data = int(input("Enter a number :"))

except:
	print("Not a valid input.!")

# Finally gets executed if the control gets out of the try block in any condition whether there is error or no_error
finally:
	print("Input attempted.")

""" This code will be in error in such cases, suppose user inputs such string which cannot be converted into
some integer, the control will go into except block:

output:
Enter a number : Ten
Not a valid input.!
Input attempted

Enter a number : 10
Input attempted """