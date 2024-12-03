# single linked list

def rev(str):
    l2 = []
    l1 = str.split(' ')
    print(l1)
    for i in range(len(l1)):
        print(l2)
        l2 = l2.append(l1[i][::-1])

    print(l2)
    str2 = ' '.join(l2)
    print(str2)
        

str = "hello I am learning python"
rev(str)