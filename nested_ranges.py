#Printing the prime numbers from 1-100.
for i in range(1,100+1):
    if(i>1):
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            print(i)
#Print the Factorials from 2-6
for num in range(2,7):
    fact=1
    for val in range(1,num+1):
        fact=fact*val
    print(f'Factorial of {num} is {fact}')


