#Printing -10....-1
for num in range(-10,0,1):
    print(num)

#printing -1.....-10
for num in range(-1,-11,-1):
    print(num)

#Printing the even and odd numbers(1---9).
for num in range(1,10):
    if(num%2==0):
        print(f'{num} is even.')
    else:
        print(f'{num} is odd.')

#Printing the sum of 'first 5' natural numbers.
s=0
for n in range(1,6):
    s=s+n
print(f'sum of first 5 natural numbers is {s}')

#Using (n*(n+1)/2)
input=5
ans=(input*(input+1)//2)
print(f'Sum of 1st {input} natural numbers is{ans}')

#Using sum()
n_input=10
res=(sum(list(range(1,n_input+1))))
print(f'Sum of first {n_input} namtural numbers is {res}')


#Printing average of the sum of the given natural numbers(i).
i=3
sum=0
count=0
for n in range(1,i+1):
    a=s+n
    count+=1
print(f'Average of first {i} natural numbers is {a/i}')


#Printing the factorial of a given number.
in_f=6
if(in_f>=0):
    fact=1
    for i in range(1,in_f+1):
        fact=fact*i
    print(f'Factorial of {in_f} is {fact}')
else:
    print('Invalid Input')
