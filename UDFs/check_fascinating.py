#1921
def Fascinating(num:int) -> bool:
    res= str(num*1) + str(num*2) + str(num*3)
    for ch in '123456789':
        if ch not in res:
            return False
    return True
n=int(input('Enter a number: '))
print(f'{n} is {"a fascinating" if Fascinating(n) else "not a fascinating"} number')