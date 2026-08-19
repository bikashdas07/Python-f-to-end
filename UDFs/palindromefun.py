def Palindrome(num : int) ->bool:
    dup=num
    rev=0
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev==dup

n=int(input("Enter the number: "))
num=n
if(num>=0):
    ans=Palindrome(num)
else:
    ans=Palindrome(abs(num))
print(f'The number {num} is {"a palindrome" if ans else "not a palindrome"}')