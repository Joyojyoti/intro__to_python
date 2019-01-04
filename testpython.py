items = ['first string', 'second string', 'third string']
"""This is a list of strings for a html page"""
print("<ul>")
for item in  items:
	result = "<li>{}</li>".format(item) #.format(item) will replace '{}' by value of the string 'item'
	print(result)

print("</ul>")
"""The following output will be like:
<ul>
<li>first string</li>
<li>second string</li>
<li>third string</li>
</ul>"""

