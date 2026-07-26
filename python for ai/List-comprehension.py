# List Comprehension 

# Add 1 to 10 numbers to a list 

L = [i for i in range (1,11)]
print (L)

# Scalar Multiplication on a vector 
  
L = [1,2,3]
s = -3 
r = [s*i for i in L]
print(r)

# Add Squares 

L = [1,2,3,4,5]

s = [i**2 for i in L]
print(s)

# Print all the numbers divisible by 5 in the range of 1 to 50

l = [i for i in range (1,51) if i%5 == 0]
print(l)

# find languages which start with letter p

languages = ['java', 'python', 'php', 'c', 'javascript']
l = [language for language in languages if language.startswith('p')]

print(l)

# Nested if with list Comprehension 

basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'graphes', 'banana']
 add new list from my_fruits and items if the fruit exists in basket and also start with "a"

f = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
print(f)
#  normal way 
for fruit in basket:
    if fruit in my_fruits :
        print(fruit, fruit.startswith("a"))
    else :
        print("no")

# print a (3,3) matrix using list comprehension (nested list)

m = [[i*j for i in range (1,4)] for j in range (1,4)]

print(m)

#  cartesian product 

L1 = [1,2,3,4]
L2 = [5,6,7,8]       

l=[i*j for i in L1 for j in L2]
print(l)
