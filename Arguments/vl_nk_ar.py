def Sample(*args): #Returns {Tuple,}
    print(args)
    print(args[0]+args[1])
Sample(10, 20, 30)
Sample(1,2,3,4,5,6,7,8,9)
Sample(50,5)
#Sample() -Remove 1st print statement to avoid IndexError.
Sample(10,20,30,40,50,60,70,80,90,100) 
#Sample(a=10, b=20, c=30) - Keyword arguments can't be used with variable length non-keyword arguments.