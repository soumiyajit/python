"""
WAP to search the number of times a particular number occurs in list
"""

def num_count(l,num):
    count = 0
    for i in range(0,len(l)):
        if l[i] == num:
            count = count + 1
    return count



l1 = [3,5,7,3,6,9,1,2,22,4,2,3,3,4,2,4,6,7,4,5,3,5]
print num_count(l1,3)

