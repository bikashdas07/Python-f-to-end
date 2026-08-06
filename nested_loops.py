#Nested for-loops.

for val1 in range(1,5):
    for val2 in range(11,15):
        print(val2)
        #print(val1)
        #print(val1,val2)

for val1 in range(1,5):
    for val2 in range(11,15):
        print(val1,val2)
        break

for val1 in range(1,5):
    for val2 in range(11,15):
        print(val1,val2)
    break

for val1 in range(1,5):
    break
        for val2 in range(11,15):
            print(val1,val2)
