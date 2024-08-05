num1= int(input("enter the number ; "))
num = 2
x=num
def isprime(num):
    for i in range (2,num):
        for j in range (2,i):
            if (i %j ==0):
                break

        else:
            return i
while (num1>0):
     for i in range (1,num):
         print(isprime(i))

     num+=1
     num1=num-1
         
    
    
