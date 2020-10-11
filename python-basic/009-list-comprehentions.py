"""

Use list comprehentions to print the square of all odd numbers from 1-10

"""

list_comp = [i**2 for i in range(1,11) if i%2 == 1]
print list_comp
