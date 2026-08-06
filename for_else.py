#For:else:- loop
for var in range(1,5):
    print(var)
    #break
    #continue
    #pass
else:
    print('else-block of for')


#for with break-keyword
    
#1
for var in range(1,5):
    if(var==3):
        break
    else:
        print(var)
print('Outside for loop')

#2
for i in range(1,5):
    if(i==3):
        break
    print(i)
else:
    print('else-block(not executable)')
print('Outside for-else loop')

#3
for num in range(1,5):
    break
    print(num)
else:
    print('else-block(not executable)')
print('Outside for-else loop')

#4
'''
for num in range(1,5):
    print(num)
else:
    print('Throws error beacause break is in else block.')
    break
'''




