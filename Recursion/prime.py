def Prime(num, i=2):
    if i*i > num:
        return True
    return False if num % i == 0 else Prime(num, i + 1)

n=int(input('Enter the number: '))
num=n
if n>1:
    print(f'{n} is {"prime" if Prime(num)==True else "Not prime"}')
else:
    print("Can't check")