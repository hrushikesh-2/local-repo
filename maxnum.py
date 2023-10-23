def maxnum(list):
    max=list[0]
    for i in range(0,len(list)): 
        if(max<list[i]):
            max=list[i]
    return max 
print("enter elements in list")
list=[10]
for i in range(0,10):
    a=int(input("enter value:"))
    list.append(a)
print("maximum value in entered list is:",maxnum(list))