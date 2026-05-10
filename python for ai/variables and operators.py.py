# 100 day Revision of Python 
# day 1: Variables and Data Types

name = "Rohit Malik" # name = variable, "Rohit Malik" = String
age = 20             # age = variable, 20 = Integer
height = 5.9         # height = variable, 5.9 = Float
print("My name is: ", name)
print("Age: ", age)
print(type(name))
print(type(age))
print(type(height))
old = False
print("Is Rohit old? ", old)
print(type(old))

# types of operators in Python
# 1. Arithmetic Operators: +, -, *, /, %, //, **
a = 10
b = 3
print("a + b = ", a + b) # 13
print("a - b = ", a - b) # 7 
print("a * b = ", a * b) # 30
print("a / b = ", a / b) # 3.33333333333
print("a % b = ", a % b) # 1
print("a // b = ", a // b) # 3
print("a ** b = ", a ** b) # 1000

# 2. Comparison Operators: ==, !=, >, <, >=, <=
c = 10
d = 20
print("c == d = ", c == d) # False
print("c != d = ", c != d) # True
print("c > d = ", c > d) # False
print("c < d = ", c < d) # True
print("c >= d = ", c >= d) # False
print("c <= d = ", c <= d) # True

# 3. Logical Operators: and, or, not
e = True
f = False
print("e and f = ", e and f) # False
print("e or f = ", e or f) # True
print("not e = ", not e) # False

# 4. Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=
g = 5      
g += 2 # g = g + 2
print("g += 2: ", g) # 7    
g -= 3 # g = g - 3
print("g -= 3: ", g) # 4
g *= 4 # g = g * 4
print("g *= 4: ", g) # 16
g /= 2 # g = g / 2
print("g /= 2: ", g) # 8.0
g %= 3 # g = g % 3
print("g %= 3: ", g) # 2.0
g //= 2 # g = g // 2
print("g //= 2: ", g) # 1.0
g **= 3 # g = g ** 3
print("g **= 3: ", g) # 1.0
