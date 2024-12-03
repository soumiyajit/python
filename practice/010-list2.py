"""

list the lower charenters of all the alphbets in the list
extract number from a string

"""

print[x.lower() for x in ["A","B","C","Sam","xYZ"]]

string = "test the numers - 12345 test again 007"
l2 = [x for x in string if x.isdigit()] 
print ''.join(l2)