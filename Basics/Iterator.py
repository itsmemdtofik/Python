
#! Python Iterator

mytuple = ("apple", "banana", "cherry")
it = iter(mytuple)

print(next(it))
print(next(it))
print(next(it))
#print(next(it)) #Raise an error Stop Iteration

#! String also iterable

string = "banana"
it = iter(string)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) #StopIteration

#! How for loop uses iterator

print("How for loops uses an iterator")
numbers = [1, 2, 3, 4]
it = iter(numbers)

while True:
    try:
        num = next(it)
        print(num) #Output: 1, 2, 3, 4
    except StopIteration:
        break

#! How to create a custom iterator

print("How to create a custom iterator")
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):  # Must return the iterator object
        return self

    def __next__(self):  # Must return next value or raise StopIteration
        if self.current <= 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

# Using the iterator
countdown = CountDown(3)
for num in countdown:
    print(num)  # Output: 3 2 1