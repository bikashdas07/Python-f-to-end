num=int(input('Enter the maximun range: '))
for n in range(1,num+1):
    if(n%5==0):
        print('FizzBuzz')
    elif(n%3==0):
        print('Buzz')
    elif(n%2==0):
        print('Fizz')
    else:
        print(n)
 
