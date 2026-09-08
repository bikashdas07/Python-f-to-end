def Sample(a=100, b=200, c=300):
    print(a, b, c ,sep=' ')
Sample(10, 20, 30)
Sample(1, 2)
Sample(11)
Sample()
Sample(1,b=20)
Sample(10, c=40)
Sample(b=200, c=30)
#Sample(a=10, b=20, 30) - Positional arguments can't follow keyword arguments.
#Sample(10, a=10, b=20, c=30) - Arguments count mismatch with parameters count.
#Args<=Params