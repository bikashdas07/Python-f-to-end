def Sample(a,b,c):
    print(a, b, c ,sep=' ')
a=10
Sample(a=10, b=20, c=30)
Sample(10, b=10, c=30)
Sample(10, 20, c=a)
Sample(10, 20, c=30)
# Sample(a=10, b=20, 30) Sample (a=10, 10, c=20)- Positional arguments can't follow keyword arguments.
