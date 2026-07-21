#Convert a given Integer into Binary
i=int(input(" Enter an integer: "))
dup=i
i=abs(i)
temp=i
place=1
b=0
while(i>0):
    rem=i%2
    b=b+rem*place
    place*=10
    i//2
if dup>0:
    print(f"Binary of {temp} is {b}")
else:
    print(f"Binary of {dup} is -{b}")
    
    
#Using Built in function.
print(bin(i))