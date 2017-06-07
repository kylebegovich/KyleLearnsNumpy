"""Basic builtins, syntax, functions to keep in mind, etc."""

#  type( var )  returns the type, since it's dynamic, this can be used for polymorphism
print("\nUsing type():")
x = 8
y = 8.0
print(type(x), type(y), type([x, y]), type((x, y)), type({x, y}))


#  Operators:  exponentiation, logical and, logical or, logical not, logical XOR
print("\nUsing operators:")
t = True
f = False
print(2 ** 5, 3 ** 2)
print(t and t, t and f, f and t, f and f)
print(t or t, t or f, f or t, f or f)
print(t, not t, f, not f)
print(t != t, t != f, f != t, f != f)


#  Strings, full reference : https://docs.python.org/3.5/library/stdtypes.html#string-methods
print("\nUsing strings:")
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

# splitting a string based off of some character / delimiter; gets rid of the splitting parameter
sentence = "The quick, brown fox jumped over the, lazy, dog."
print(sentence.split(' '))
print(sentence.split(","))
print(sentence.split(" ", 5))  # max number of splits specified
print(sentence.split("brown"))  # can be whole word / phrase doing the split

# other fun stuff
print(string1.capitalize())  # Capitalize a string; prints "Hello"
print(string1.upper())       # Convert a string to uppercase; prints "HELLO"
print(string1.rjust(7))      # Right-justify a string, padding with spaces; prints "  hello"
print(string1.center(7))     # Center a string, padding with spaces; prints " hello "
print(string1.replace('l', '(ell)'))  # Replace all instances of one substring with another; prints "he(ell)(ell)o"
print('  world '.strip())  # Strip leading and trailing whitespace; prints "world"
