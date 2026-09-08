def Perfect(start):
    if num==0:
        return 0
    if start < num:
        if num%Perfect(start+1) == 0:
         return start
        return 0
n=int(input('Enter the number: '))
num=n
start=1
if n>0:
    print(f'{n} is {'perfect' if Perfect(start)==n else 'Not Perfect'}')