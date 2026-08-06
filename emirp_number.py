#Check wheteher a given number is EMIRP-NUMBER or not.(Number should be prime, Reverse should be prime, Not a palindrome)
num=int(input('Enter the number: '))
if(num>=2):
    for val in range (2,int((num**0.5)+1)):
        if(num%val == 0):
            print(f'{num} is not EMIRP number.')
            break
    else:
        digit=0
        dup=num
        while(num!=0):
            rem=num%10
            digit=digit*10+rem
            num//=10
        if(digit==dup):
            print(f'{dup} is not EMIRP number.')
        else:
            for val in range (2,int((digit**0.5)+1)):
                    if(digit%val == 0):
                        print(f'{dup} is not EMIRP number.')
                        break
            else:
                print(f'{dup} is EMIRP number')
else:
    print('Not a EMIRP number.')