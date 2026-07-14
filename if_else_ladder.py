#Highest among 3 numbers.
n1,n2,n3= 10,20,32
if(n1==n2 and n2==n3):
    print("All numbers are equal")
else:
    if (n1>n2):
        if(n1>n3):
            print("n1 is the largest number")
        else:
            print("n3 is the largest number")
    else:
        if(n2>n3):
            print("n2 is the largest number")
        else:
            print("n3 is the largest number")
            
            
#Effective solution using elif.
if(n1==n2==n3):
    print("All numbers are equal")
elif(n1>n2 and n1>n3):
    print("n1 is the largest number")
elif(n2>n3):
    print("n2 is the largest number")
else:
    print("n3 is the largest number")



#Highest among 4 numbers.
n1,n2,n3,n4= 10,20,32,11
if(n1==n2 and n2==n3 and n3==n4):
    print("All numbers are equal")
else:
    if(n1>n2):
        if(n1>n3):
            if(n1>n4):
                print("n1 is the largest number")
            else:
                print("n4 is the largest number")
        else:
            if(n3>n4):
                print("n3 is the largest number")
            else:
                print("n4 is the largest number")
    else:
        if(n2>n3):
            if(n2>n4):
                print("n2 is the largest number")
            else:
                print("n4 is the largest number")
        else:
            if(n3>n4):
                print("n3 is the largest number")
            else:
                print("n4 is the largest number")
                
                
#Effective solution using elif.
if(n1==n2==n3==n4):
    print("All numbers are equal")
elif(n1>n2 and n1>n3 and n1>n4):
    print("n1 is the largest number")
elif(n2>n3 and n2>n4):
    print("n2 is the largest number")
elif(n3>n4):
    print("n3 is the largest number")
else:
    print("n4 is the largest number")