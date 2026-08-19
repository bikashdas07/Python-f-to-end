def factorial():
    fact = 1
    for var in range(1,n+1):
        fact=fact*var
    return fact

n=int(input('Enter a number: '))
print(f'The factorial of {n} is {factorial()}') 
        