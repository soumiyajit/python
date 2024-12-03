"""

Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

"""

def prime(limit):
    if (limit <= 0):
        print("limit showuld be greater than 0 ")
        quit()
    elif (limit == 1):
        print ("1 is not a prime number")
        quit()

    for i in range(2,limit+1):
        flag = 0
        for j in range(2,i):
            if (i%j == 0):
                flag = 1
                break
        if (flag == 0):
            print(i),
    

limit = input ("Enter the number:")
prime(limit)


