#Check wheteher a given number is palyprime or not.(Both palindrome and prime)
num=int(input('Enter the number: '))
if(num>=2):
    for val in range (2,int((num**0.5)+1)):
        if(num%val == 0):
            print(f'{num} is not palyprime.')
            break
    else:
        digit=0
        dup=num
        while(num!=0):
            rem=num%10
            digit=digit*10+rem
            num//=10
        if(digit==dup):
            print(f'{dup} is palyprime.')
        else:
            print(f'{dup} is not palyprime.')
else:
    print('Not a palyprime.')