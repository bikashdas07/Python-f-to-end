#Print the reverse of a number and check whether it's Plaindrome or Not.
num=int(input("Enter the number: "))
dup=num
num=abs(num)
temp=num
digit=0
while(num!=0):
    rem=num%10
    digit=(digit*10) + rem
    num//=10
if dup<0:
    print(f'Reverse of -{temp} is -{digit}')
else:
    print(f'Reverse of {temp} is {digit}')

if(digit==temp):
    print(f'{temp} is a palindrome number.')
else:
    print(f'{temp} is not a palondrome number.')