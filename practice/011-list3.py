"""

list of list for mutiplication table

"""

def multi_table(a):
    multi = [[a,b,a*b] for b in range(1,11)]
    return multi


print multi_table(5)