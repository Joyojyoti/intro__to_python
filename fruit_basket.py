# This is a dictionary of itenms that are bought with the key values which actually shows the number of items
basket_items = {'orange':5 , 'banana':10, 'tubes':10, 'screw':20}

# This is the list oif fruits
fruits = ['orange','banana','grapes']
in_fruit = 0
not_in_fruit = 0

for fruit,count in basket_items.items():
	if fruit in fruits:
		in_fruit += count

	else:
		not_in_fruit += count


print(basket_items)
print(in_fruit)
print(not_in_fruit)

#This code will print how many fruits are being taken and how many non_fruits are being taken
