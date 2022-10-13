class Underscore:
    def map(self, iterable, callback):
        # your code here
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable

    def find(self, iterable, callback):
        # your code here
        for num in iterable:
            if callback(num):
                return num
        return False

    def filter(self, iterable, callback):
        # your code
        new_list = []
        for num in iterable:
            if callback(num):
                new_list.append(num)
        return new_list

    def reject(self, iterable, callback):
        # your code
        new_list = []
        for num in iterable:
            if not callback(num):
                new_list.append(num)
        return new_list

    def reduce(self, iterable, callback):
        # your code
        new_list = []
        total = 0
        for i in iterable: 
            new_list.append(callback(i))
        for j in new_list:
            total += j
            
        return total

# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore

print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]
print( _.reduce([47,11,42,13], lambda x: x**2)) # should return 4263