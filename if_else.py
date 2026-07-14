if True: print('Pedro')
if 0:
    print('Bison')

num= 0
if(num%2==0):
    print('Even')
else:
    print('Oddd')

Monday= False
if(Monday):
    print(2+3)



#No extra statements in between.    
else:
    print('LazyDay')


if(True!=False):print('True')
else:print('False')


if(False!=0):print('if block')
elif(True==1):print('elif block') 
else: print('else block')


if(1!=True):
    print('if true')
elif(0!=False):
    print('1st elif')
elif(0!=1):
    pass
else:
    print('else block')


if (1,):
    print('Tuple-1')
    if(1==True):
        print('1')
        if(0==1):
            print('Nested if')
        elif(0!=False):
                print('0')
        else:
            print('Nested')
    elif(0!=1):
        print('')
    else:
        print('elif ladder')
else:
    print('Something')
