def Outer(arg):
    print(f'hello1{arg}')
    def Inner():
        print(f'hello3{Inner}')
        return arg()
    return Inner
@Outer #->Outer(M1)
def M1():
    print('hello4')
print(f'hello2{M1}')
M1()