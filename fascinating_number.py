#Find wheteher a number is fascinating or not.
#e.g. 191-> (192*1)=192,(192*2)=384,(192*3)=576
#192384576
#All the digits from 1-9 are present.

n=int(input('Enter a number: '))
res=str(n*1)+str(n*2)+str(n*3)
print(f"The number's fascination is {res}")
for i in range(1,10):
    if(str(i) not in res):
        print('Non-Fascinating Number.')
        break
else:
    print('Fascinating number.')
