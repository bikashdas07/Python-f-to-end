'''
return is much more than the function itself.
Technically, return is the last statement of a function, 
and it is used to send the result of the function back to the caller.
When a function is called, 
it executes its code and then returns a value (if specified) to the point where it was called. 
The return statement can also be used to exit a function early,
before reaching the end of the function's code.
'''
def sample():
    print('Hello')
    return 10
    print('World')#- This line will not be executed as the function will return before this line is reached.

sample()
print('--')
var =sample()
print(var) 
 
def sample():
    print('Hello')
    return 10
    print('World')#- This line will not be executed as the function will return before this line is reached.

sample()
print('--')
var =sample()
print(var) 

def sample():
    print('Hello')
    return 10,20,False,[1,2,3]
    print('World')#- This line will not be executed as the function will return before this line is reached.

var=sample()
print(var) 
