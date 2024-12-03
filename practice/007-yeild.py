"""

WAP to print the square all numbers from 1-100 using yeild.

"""

def square_generator():
    for i in range(1,101):
        yield(i*i)

for value in square_generator():
    print value,