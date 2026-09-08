'''
Eucledian's principle
gcd(a,b)=gcd(b,a%b)
a*b=gcd(a,b)*lcm(a,b)
'''
'''
import math
math.lcm(a,b)
'''

def lcm(a, b):
    return a*b //gcd(a,b)
def gcd(a,b):    
    while b!=0:
        a,b=b,a%b
    return a

    '''while b==0:
        return a
    gcd(b,a%b)'''

num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
a,b=num1,num2
ch=input('Enter the choice for lcm or gcd or both: ')
if ch=='lcm':
    print("lcm of the given numbers are: ",lcm(a,b))
elif ch=='gcd':
    print("gcd of the given numbers are: ",gcd(a,b))
elif ch=='both':
    print("lcm of the given numbers are: ",lcm(a,b))
    print("gcd of the given numbers are: ",gcd(a,b))
else:
    print("Invalid choice") 