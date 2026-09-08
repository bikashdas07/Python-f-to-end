#13,17,31,37,71,73,79,97
def Prime(num: int) -> bool:
    for var in range(2,int(num**0.5)+1):
        if num%var==0:
            return False
    return True

def NotPalindrome(num: int) -> int:
    res=0
    while (num>0):
        res=res*10+num%10
        num//=10
    return res   
def EMIRP(num: int) -> str:
    rev=NotPalindrome(num)
    f= (f'{n} is {'an EMIRP number' if Prime(num) and rev!=n and Prime(rev) else  'not an EMIRP number'}')
    return f
n=int(input('Enter the number: '))
num=n
if (num>1):
    print(EMIRP(num))
else:
    print('Not an EMIRP number')