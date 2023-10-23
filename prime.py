list=[1,2,3,4,5,6,7]
for i in list:
    if (i==0 or i==1):
        continue
    else:
        for j in range(2,i-1):
            if(i%j==0):
                break
        else:
            print("prime numbers are :",i)
        
    
        