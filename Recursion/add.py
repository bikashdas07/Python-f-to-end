def Add(s):
    if s==e+1:
        return 0
    return s+Add(s+1)
s=int(input('Enter the starting range: '))
e=int(input('Enter the ending range: '))
print(Add(s))
Add(s)