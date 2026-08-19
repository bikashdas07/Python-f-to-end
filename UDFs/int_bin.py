def int_bin(num:int) -> str:
    dup=num
    num=abs(num)
    place=1
    b=0
    while(num>0):
        rem=num%2
        b=b+rem*place
        place*=10
        num//=2
    if dup>0:
        return '0b'+str(b)
    return '-0b'+str(b)
    #return bin(num)

num=int(input(" Enter an integer: "))
print(int_bin(num))