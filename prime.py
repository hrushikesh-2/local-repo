list=[1,2,3,4,5,6,7]
for i in range(0,len(list)):
    for i in range(2,len(list)-1):
        if(n%i==0):
            break
    else:
        print("Prime numbers are:"list(i))
        