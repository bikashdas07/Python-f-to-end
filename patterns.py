#Vertical *
num = 5
print('Vertical')
for _ in range(1,num+1):
    print('*')
 
#Horizontal *
print('Horizontal')
for _ in range(num):
    print('*',end='')
for _ in range(num):
    print('*','*',sep='&')

#Stars
max=5
print('Using Escape Sequence')
for _ in range(1,5):
    for _ in range(1,5):
        print('*',end=' ')
    print()
#Hallow Square
hallow=int(input('Enter the hallow string range(Max): '))
for row in range(1,hallow+1):
    for col in range(1,hallow+1):
        if(row==1 or col==1 or row==hallow or col==hallow):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#Rectangle
rows = int(input('Enter the number of rows: '))
cols=rows*2
print('Solid Rectangle')
for row in range(1,rows+1):
    for col in range(1,cols+1):
        print('*',end=' ')
    print()
print('Hallow Rectangle')
for row in range(1,rows+1):
    for col in range(1,cols+1):
        if(row == 1 or col == 1 or row == rows or col == cols):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
