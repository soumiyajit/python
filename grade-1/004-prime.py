def prime(min,max):
    l1 = []
    for i in range(min,max):
        for j in range(2,i-1):
            if(i%j) == 0:
                break

        else:
            l1.append(i)

    print(l1)


prime(1,100)