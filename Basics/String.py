x = 'Hello, World!'

print(x.upper())
print(x.lower())
print(x.strip())
print(x.split(','))
print(x.replace('e','a'))


#Concotenating string

#This wont work
'''age = 25
txt = 'My name is Jhon, I am ' + age
print(txt)'''

#We use the F-String method to solve this issue
age = 34
txt = f'My name is Jhon, I am {age}'
print(txt)


x = 'abababa'

for i in x:
    print(i)

if 'z' not in x:
    print("Not there")

print(x[1])
print(len(x))