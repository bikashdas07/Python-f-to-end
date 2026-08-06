#Check whether the given number is prime or not.
num=int(input('Enter the number: '))
if(num>=2):
    for i in range (2,(num//2+1)):
        if(num%i == 0):
            print(f'{num} is not prime.')
            break
    else: 
        print(f'{num} is Prime.')
else:
    print(f'{num} is not prime.')

#Effective solution(Iterating upto sqrt())
if(num>=2):
    for i in range (2,int((num**0.5)+1)):
        if(num%i == 0):
            print(f'{num} is not prime.')
            break
    else: 
        print(f'{num} is Prime.')
else:
    print(f'{num} is not prime.')