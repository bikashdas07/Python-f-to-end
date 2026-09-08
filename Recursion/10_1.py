def Sample(num):
    if num<1:
        return
    print(num)
    Sample(num-1)
Sample(10)