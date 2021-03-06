"""Basic builtins, syntax, functions to keep in mind, etc."""
import math


#  Operators:  exponentiation, logical and, logical or, logical not, logical XOR
print("\n\nUsing operators:")
t = True
f = False
print(2 ** 5, 3 ** 2)
print(t and t, t and f, f and t, f and f)
print(t or t, t or f, f or t, f or f)
print(t, not t, f, not f)
print(t != t, t != f, f != t, f != f)


#  Strings, full reference : https://docs.python.org/3.5/library/stdtypes.html#string-methods
print("\n\nUsing strings:")
# definition, either is acceptable
string1 = "hello"
string2 = 'world'
print(string1, string2)

# concatenation, with or without literals is acceptable, "Java style"
hw = string1 + ' ' + string2 + "!"
# concatenation, with or without literals, "sprintf or C style"
hw2 = "%s %s part %d!" % (string1, string2, 2)
print(hw, hw2)

# getting length of a string, or other container object
print(string1, len(string1))

# conversions into string from other types
print(804, str(804), type(804), type(str(804)))
print(80.4, str(80.4), type(80.4), type(str(80.4)))

# splitting a string based off of some character / delimiter; gets rid of the splitting parameter
sentence = "The quick, brown fox jumped over the, lazy, dog."
print(sentence.split(' '))
print(sentence.split(","))
print(sentence.split(" ", 5))  # max number of splits specified
print(sentence.split("fox"))  # can be whole word / phrase doing the split

# other fun stuff
print(string1.capitalize())  # Capitalize a string; prints "Hello"
print(string1.upper())       # Convert a string to uppercase; prints "HELLO"
print(string1.rjust(7))      # Right-justify a string, padding with spaces; prints "  hello"
print(string1.center(7))     # Center a string, padding with spaces; prints " hello "
print(string1.replace('l', '(ell)'))  # Replace all instances of one substring with another; prints "he(ell)(ell)o"
print('  world '.strip())  # Strip leading and trailing whitespace; prints "world"


#  type( var )  returns the type, since it's dynamic, this can be used for polymorphism
print("\n\nUsing type():")
x = 8
y = 8.0
print("x = 8 is of type: ", type(x))
print("y = 8.0 is of type: ", type(y))
print("[x, y] = [8, 8.0] is of type: ", type([x, y]))
print("(x, y) = (8, 8.0) is of type: ", type((x, y)))
print("{x, y} = {8, 8.0} is of type: ",type({x, y}))


#  Containers
print("\n\nUsing Containers:\nLists:")
# lists in python are mutable arrays : https://docs.python.org/3.5/tutorial/datastructures.html#more-on-lists
list1 = [1, 2, 3]
print(list1, list1[0], list1[-1])  # negative indices count back from the end, where list[length-1] = list[-1]
list1[1] = "woah"   # not hard-typed
print(list1)
list1.append(("can", 'contain', "tuples!"))
list1.insert(1, 2)   # can insert at different locations in the list
print(list1)
first = list1.pop(0)   # pop from a certain index
print(first, list1)
list1.remove(2)   # or remove a certain item from the list
print(list1)

# slicing
nums = list(range(0, 5, 1))
print(nums)
print(nums[1:3])  # choose start and end points for a sublist (slice of list)
print(nums[2:])  # can go from index to end
print(nums[:2])  # can go from start to index
print(nums[:-2])  # indexes can be negative
print(nums[:])  # yeah, this is whatever
nums[2:4] = [8, 9]  # can replace a slice with another list
print(nums)
nums[2:4] = [7]  # sizes don't have to match, but you won't replace the entire sublist
print(nums)
nums[2:3] = [9, 8, 6]  # but you can make the list bigger by replacing a smaller slice
print(nums)

# list looping, effectively for-each loops
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
for letter in my_list:
    print(letter, letter.capitalize())
my_list = ['birdue', 'doggo', 'puppor', 'meowser']
for index, animal in enumerate(my_list):
    print ("animal #%d is: %s" % (index, animal))

# list comprehensions
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)
# equivalent to:
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)
# can also contain conditionals
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)

# Dictionaries
print("\nDictionaries:")
my_dict = {"start": (0, 0), "end": (4, 5)}
print("start : ", my_dict["start"])  # reference of a value
my_dict["trap"] = (3, 3)  # assigning a new key/value pair
print("is the trap in my_dict?", "trap" in my_dict)  # checks for belonging to the container, true
print("trap : ", my_dict["trap"])
#  print(my_dict["hole"])  will not evaluate, throws an error
print("The hole is at:", my_dict.get("hole", (-1, -1)))  # instead, use get() with a default
print("The trap is at:", my_dict.get("trap", (-1, -1)))


# get() is equivalent to the following function:
def my_get(dictionary, key, default):
    if key in dictionary:
        return dictionary[key]
    else:
        return default

print("The hole is at:", my_get(my_dict, "hole", (-1, -1)))
print("The trap is at:", my_get(my_dict, "trap", (-1, -1)))

del my_dict["end"]  # removes the pair from the structure
print("The end is at:", my_dict.get("end", (-1, -1)))
#  del my_dict["hole"]  throws an error as well, accessing out of bounds / not in container

# looping dictionaries:
print("Loops:")
my_dict = {'horses': 2,'sloths': 3, 'birds': 4, 'people': 5}
for species in my_dict:
    toes = my_dict[species]
    print("%s have %d toes on each foot" % (species, toes))

my_dict = {'cyclops': 1, 'human': 2, 'dragonfly': "too many"}  # can do different types for values
for creature in my_dict:
    eyes = my_dict[creature]
    message = "A %s has %s eye" % (creature, str(eyes))  # can set all values to one type as a work-around
    if not eyes == 1:
        print(message + "s")
    else:
        print(message)

# dictionary comprehensions
print("Comps:")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num_to_two_pow = {x: 2 ** x for x in nums if x % 2 == 0}  # creating a map based of a list comprehension
print(even_num_to_two_pow)

square_nums_to_their_root = {s: int(math.sqrt(s)) for s in nums if math.sqrt(s) == math.floor(math.sqrt(s))}
print(square_nums_to_their_root)  # can use imported functions within comprehensions


# Sets
print("\nSets:")
animals = {'cat', 'dog'}
print('cat' in animals)  # Check if an element is in a set
print('fish' in animals)
animals.add('fish')  # Adding an element to a set
print('fish' in animals)
print(len(animals))
animals.add('cat')  # Adding an element that's already belonging to the set is a no-op
print(len(animals))
animals.remove('cat')  # Remove element from the set
print(len(animals))

# Iterating over sets: same as a list, but order is not guaranteed
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
other_animals = {'bird', 'monkey', 'tiger'}
for idx, animal in enumerate(other_animals):
    print('#%d: %s' % (idx + 1, animal))

# Set comprehensions are a thing
nums = {int(math.sqrt(x)) for x in range(30)}  # the sqrt of all numbers 0 - 29, truncated not rounded
print(nums)
nums = {math.floor(math.log(x, 2)) for x in range(1, 65)}
print(nums)


# Tuples : immutable little lists
print("\nTuples:")
t = (5, 6)        # Create a tuple
d = {(x, x + 1): x for x in range(7)}  # Create a dictionary with tuple keys
print(t, type(t))
print(d)
print(d[t])
print(d[(1, 2)])
t = ("types", 5, "dont", 8.0, 'matter')  # even inside of other containers!
print(t)
d = {t: 123, (1, 1, 0): 6, (1, 1): 3}
print(d)


# Functions
print("\n\nFunctions:")


def sign(x):
    """ with functional comment style too! """
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))


def hello(name, loud=False):
    """ We can take optional arguments as well, kinda polymorphism? yeah"""
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s' % name)

hello('Bob')
hello('Fred', True)
hello("Kyle", loud=True)
hello("Cinder", loud=False)


def wat(a, b):
    """ pass in tuples with an extra set of parentheses """
    if a > b:
        return True
    elif a < b:
        return -17
    elif a ** b > math.pi:
        return "Returns are a different beast in Python"
    else:
        return

for t in [(1, 0), (0, 1), (3, 3), (0, 0)]:
    print(wat(t[0], t[1]))


# Classes
class Greeter(object):

    # Constructor uses builtin __init__
    def __init__(self, name):
        self.name = name  # Create and store an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

    # Class methods
    @staticmethod
    def introduce():
        print("Hello!, my name is Python.")

g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()
g.greet(True)
g.introduce()
