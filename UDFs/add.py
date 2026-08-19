def Add():
    res=0
    for i in range(1,n):
        res=res+i
    return res

n=int(input('Enter a number: '))
sum=Add()
print(f'Sum is {sum}')

def Add_num(n):
    res=0
    while(n>0):
        res=res+n
        n=n-1
    return res

n=int(input('Enter a number: '))
sum=Add_num(n)
print(f'Sum is {sum}')