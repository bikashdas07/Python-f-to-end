#Syntax: for (variable in range()/collection_datatypes, collection_object):
l=[1,'Money',3.5,True]
for i in l:
    print(f'{i} : {type(i)}')

t=(10,'Messi', True, (3+4j))
for j in t:
    print(f'{j} : {type(j)}')
 
s={12,34,(56,78)}    
for keys in s:
    print(f'{keys} : {type(keys)}')

D={'Name':'Pedro','Age':25,'Country':'India'}
for key in D:
    print(f'{key} : {D[key]}')

#Vowels in a string.    
s='engineering'
for ch in s:
    if ch in 'aeiouAEIOU':
        print(f'{ch}')

#Remove duplicate characters from a string.
s='engineering'
ans=''
for ch in s:
    if ch not in ans:
        ans=ans+ch
print(ans)

#Reverse a string using for loop.
s='engineering'
ans=''
for ch in s:
    ans=ch+ans
print(ans)

#Palindrome
s='malayalam'
ans=''
for ch in s:
    ans=ch+ans
if(s==ans):
    print('Palindrome')
else:
    print('Not Palindrome')
