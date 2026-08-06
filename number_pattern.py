num=int(input('Enter the no. or rows: '))
for row in range(1,num+1):
    for col in range(1,num+1):
        print('1',end=' ')
    print()
        
for row in range(1,num+1):
    for col in range(1,num+1):
        print(row,end=' ')
    print()

for row in range(num,0,-1):
    for col in range(1,num+1):
        print(row,end=' ')
    print()

for row in range(1,num+1):
    for col in range(num,0,-1):
        print(col,end=' ')
    print()

for row in range(1,num+1):
    for col in range(1,row+1):
        print(col,end=' ')
    print()

for row in range(num,0,-1):
    for col in range(1,row+1):
        print(col,end=' ')
    print()
 
    
for row in range(1,num+1):
    for col in range(row,0,-1):
        print(col,end=' ')
    print()


for row in range(num,0,-1):
    for col in range(row,0,-1):
        print(col,end=' ')
    print()


for row in range(num,0,-1):
    for col in range(row,num+1):
        print(col,end=' ')
    print()
spaces=num-1
for row in range(num,0,-1):
    for col in range(1,spaces+1):
        print(' ',end=' ')
    for col2 in range(row,num+1):
        print(col2,end=' ')
    print()
    spaces-=1

spaces=num-1
for row in range(1,num+1):
    for col1 in range(1,spaces+1):
        print(' ',end=' ')
    for col2 in range(row,0,-1):
        print(col2,end=' ')
    print()    
    spaces-=1
spaces=0
for row in range(1,num+1):
    for col1 in range(1,spaces+1):
        print(' ',end=' ')
    for col2 in range(num,row,-1):
        print(col2,end=' ')
    print()    
    spaces+=1
