def Spy(num):
    if num==0:
        return 0
    global digit_sum,digit_mul
    digit_sum+= (num%10)
    digit_mul*= (num%10)
    return Spy(num//10)
n=int(input('Enter the number: '))
num=n
digit_sum,digit_mul=0,1
res = (Spy(num))
if digit_sum==digit_mul:
    print('Spy')
else:
    print('Not Spy')

    
def spy(num):
    if num == 0:
        return 0, 1
    digit_sum, digit_product = spy(num // 10)
    return digit_sum + num%10, digit_product * num%10

n = int(input("Enter the number: "))
s, p = spy(n)
if s == p:
    print("Spy")
else:
    print("Not Spy")