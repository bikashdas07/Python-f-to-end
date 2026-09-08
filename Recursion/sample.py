def Sample(num: int):
    if num==n2+1 :
        return
    print(num)
    num+=1
    Sample(num)
n1=int(input('Start from: '))
n2=int(input('Stop before: '))
Sample(n1)