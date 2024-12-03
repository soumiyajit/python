"""

WAP to print the largets and smallest number in a list

"""

def max_min(l):
    max = min = l[0]
    for i in range(0,len(l)):
        if l[i] < min :
            min = l[i]
        if l[i] > max :
            max = l[i]
    return max, min
    

l1 = [4,27,7,220,23,2]
max_num, min_num = max_min(l1)
print (max_num,min_num)
