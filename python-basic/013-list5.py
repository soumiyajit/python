""""

WAP to to sum all the items in a list

"""

def sum(l):
    total = 0
    for i in range(0,len(l)):
        total  = total + l[i]
    return total

l1 = [23,7,8,48]
print sum(l1)