#Step-Stars
num=int(input('Enter no. fo rows: '))
for rows in range(1,num+1):
    for cols in range(1,rows+1):
        print('*',end=' ')
    print()
#Hallow
for rows in range(1,num+1):
    for cols in range(1,rows+1):
        if(cols==1 or rows==cols or rows==num):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() 
#Inverted Step-Stars
num1=int(input('Enter no. of rows: '))
stars=num1
for row in range(1,num1+1):
    for col in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=1
#Hallow
stars=num1
for row in range(1,num1+1):
    for col in range(1,stars+1):
        #if(row==1 or col==1 or col==stars):
        if(row==1 or col==1 or col+row==num1+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    stars-=1
#Mirror-Step Stars
num2=int(input('Enter no. of rows: '))
spaces=num2-1
stars=1
for row in range(1,num2+1):
    for col1 in range(1,spaces+1):
        print(' ',end = ' ')
    for col2 in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=1
#Hallow
spaces=num2-1
stars=1
for row in range(1,num2+1):
    for col1 in range(1,spaces+1):
        print(' ',end = ' ')
    for col2 in range(1,stars+1):
        if(col2==1 or row==num2 or col2==stars):
        #if(col2==1 or row==num or row==col2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    spaces-=1
    stars+=1
#Inverted Mirror-Step Stars
num3=int(input('Enter no. fo rows: '))
spaces=0
stars=num3
for row in range(1,num3+1):
    for col2 in range(1,spaces+1):
        print(' ',end=' ')
    for col1 in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=1
    spaces+=1
#Hallow
spaces=0
stars=num3
for row in range(1,num3+1):
    for col1 in range(1,spaces+1):
        print(' ',end=' ')
    for col2 in range(1,stars+1):
        if(col2==1 or col2==stars or row==1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    stars-=1
    spaces+=1
#Pyramid
num4=int(input('Enter the no. of rows: '))
spaces=num4-1
stars=1
for row in range(1,num4+1):
    for col1 in range(1,spaces+1):
        print(' ',end=' ')
    for col2 in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=2
    spaces-=1
#Water Image
spaces=0
stars=num4+2
print('Water Image')
for row in range(1,num4+1):
    for col1 in range(1,spaces+1):
        print(' ',end=' ')
    for col2 in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=2
#Constraints.
 num=int(input('Enter the number: '))
if(num%2!=0):
    for row in range(1,num+1):
        for col in range(1,num+1):
            if(row==1 or col==1 or row==num or col==num or row==num//2+1 or col==num//2+1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
else:
    print('Not an odd number.')
#case-2
num=int(input('Enter the number: '))
if(num%2!=0):
    for row in range(1,num+1):
        for col in range(1,num+1):
            if(row==1 or col==1 or row==num or col==num
               or row==num//2+1 or col==num//2+1 or
               row==col or row+col==num+1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
else:
    print('Not an odd number.')
#case-3
num=int(input('Enter the number: '))
if(num%2!=0):
    for row in range(1,num+1):
        for col in range(1,num+1):
            if(row==1 or col==1 or row==num or col==num
               or (row==num//2+1 and col==num//2+1)):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
else:
    print('Not an odd number.')
