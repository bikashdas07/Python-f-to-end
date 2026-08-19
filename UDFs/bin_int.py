def bin_int(num : int) -> int:
    place,i=0,0
    while(num>0):
        if (num%10==1):
            i+=2**place
        num//=10
        place+=1
    return i

n=int(input(" Enter a binary number: "))
num = n
print(f"Integer of {n} is {- bin_int(abs(num)) if n<0 else bin_int(num)}")