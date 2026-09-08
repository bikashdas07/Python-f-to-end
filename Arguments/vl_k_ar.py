def Sample(**kwargs): #Returns {Dict:}
    print(kwargs['a'] + kwargs['b'] + kwargs['c'])
    print(kwargs)
Sample(a=100, b=200, c=300)
Sample(a=100, b=200, c=300, d=400)
#Sample() - Remove 1st print statement to avoid KeyError.
#Sample(10,20,a=10, b=20, c=30) - Positional arguments can't be used with variable length keyword arguments.