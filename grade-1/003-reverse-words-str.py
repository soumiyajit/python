
def rev(str1):
    l1 = str1.split(' ')
    l2 = []
    for i in range(len(l1)):
        l2.append(l1[i][::-1])
    str2 = ' '.join(l2)
    return(str2)
    


str1 = "I am coding in python"
str2 = rev(str1)
print(str2)