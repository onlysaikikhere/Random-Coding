def reverse_seq(n):
    list1.append(n)
    while (n)>1:
        n=n-1
        list1.append(n)
    return list1
list1=[]
#print(reverse_seq(5))
#print(list1)
print (str(reverse_seq(5)).replace(" ", ""))
