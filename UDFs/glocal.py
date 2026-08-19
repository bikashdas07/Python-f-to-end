print('Global Space')
num=10
def sample():
    loc=15
    print(f'Local Space- {num}')
    print(f'Local Space(loc)- {loc}')
    #num=num+1- Global variables can't be modified locally.
sample()
num=num+1
sample()
print(f'Global Space- {num}')
#print(f'Global space- {loc}')- Local variables can't be accessed outside local space

#Use of 'global' -Kw
print('Global Space')
diff=10
dup=50
def use_case():
    diff=20
    global dup
    dup = dup+10
    print(f'Local Space {diff},{dup}')
    print(f'{id(diff)} - {id(dup)}')

print(f'Global Space {diff},{dup}')
print(f'{id(diff)} - {id(dup)}')
use_case()
print(f'Global Space {diff},{dup}')
print(f'{id(diff)} - {id(dup)}')



