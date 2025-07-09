import re
line = 'This is a line'
x = re.search("^This.*line$", line)
if x:
    print("Yes! we have a match! ")
else:
    print("No match")
    