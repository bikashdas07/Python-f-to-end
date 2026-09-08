def Factorial(num):
    if num==0:
        return 1
    elif num<0:
        return 'Not Possible'
    return num*Factorial(num-1)
num=int(input('Enter the number: '))
print(Factorial(num))