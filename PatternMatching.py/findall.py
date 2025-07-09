import re
line = 'This is a line.'
x = re.findall('is',line)
print(x)

# example 2
import re
txt = 'This is a line.'
x = re.findall("sentence", txt)
print (x)

# Search function
import re 
txt = "This is a line."
x = re.search("\s", txt)
print("this frist white space character is located in the position:", x.start())



