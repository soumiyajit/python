"""

WAP to find the factorial of the number entered by the user

"""

def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result


num = input("enter a number --> ")
factorial = fact(num)
print factorial