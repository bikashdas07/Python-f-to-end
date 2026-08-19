#Prime number
def prime():
    if(n>1):
        for val in range(2,int(n**0.5)+1):
            if n%val==0:
                return 'Not Prime'
        return 'Prime'
    return 'Not Prime'

n=int(input('Enter a number: '))
print(f'The number {n} is {prime()}')

#Composite number
def composite():
    if(num>1):
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return 'Composite number'
        return 'Not a composite number'
    return 'Not a composite number'

num=int(input('Enter a number: '))
print(f'The number {num} is {composite()}')
