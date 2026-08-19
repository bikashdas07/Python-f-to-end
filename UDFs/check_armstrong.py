def check_armstrong(num:int) -> bool:
    l=len(str(num))
    dup=num
    res=0
    while(num>0):
        rem=num%10
        res=res+rem**l
        num=num//10
    return res == dup

n=int(input('Enter a number: '))
num=n
if(num>0):
    print(f"The number {n} is {'an Armstrong number' if check_armstrong(num) else 'not an Armstrong number'}.")
else:
    print(f"The number {n} is not an Armstrong number.")
