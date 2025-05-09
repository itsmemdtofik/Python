name = 'awesome'

def broapp():
    name = "fantastic"
    print("A is " + name)


broapp()
print('A is ' + name)


print('#################################################')

user = 'fantastics'
def mybroapp():
    global user
    user = 'awesome'
    print('A is ' + user)

mybroapp()
print('A is ' + user)