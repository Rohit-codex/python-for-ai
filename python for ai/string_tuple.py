# 100 day Revision of Python 
# day 4: Lists and Tuples
# List is a collection of items which is ordered and changeable. It allows duplicate members.
marks1 = 94.2
marks2 = 88.5
marks3 = 92.0
marks4 = 85.0
marks = [94.2, 88.5, 92.0 , 85.0] # using list to store marks
print(marks)
print(type(marks)) # <class 'list'>
# List operations
print("Length of marks list: ", len(marks)) # 4
print (marks[2]) # 92.0
print(marks[-1]) # 85.0
# List slicing
print(marks[1:3]) # [88.5, 92.0]
print(marks[:3]) # [94.2, 88.5, 92.0]
print(marks[1:4]) # [88.5, 92.0, 85.0]
# List methods
marks.append(90.0) # adding an element to the end of the list
print(marks) # [94.2, 88.5, 92.0, 85.0, 90.0]
marks.insert(2, 91.0) # inserting an element at index 2
print(marks) # [94.2, 88.5, 91.0, 92.0, 85.0, 90.0]
marks.remove(85.0) # removes first occurrence of an element from the list
print(marks) # [94.2, 88.5, 91.0, 92.0, 90.0]
marks.pop(4) # removes the element at index 4 from the list
print(marks) # [94.2, 88.5, 91.0, 92.0]
marks.sort() # sorts the list in ascending order
print(marks) # [88.5, 91.0, 92.0, 94.2]
marks.sort(reverse=True) # sorts the list in descending order
print(marks) # [94.2, 92.0, 91.0, 88.5]
marks.reverse() # reverses the order of the list
print(marks.reverse()) # [88.5, 91.0, 92.0, 94.2]

# Tuple is a collection of items which is ordered and unchangeable. It allows duplicate members.
tup = (94.2, 88.5, 92.0 , 85.0) # using tuple to store marks
print(tup)  # (94.2, 88.5, 92.0, 85.0)
print(type(tup)) # <class 'tuple'>
# Tuple operations
print("Length of tup: ", len(tup)) # 4
print(tup[2]) # 92.0
print(tup[-1]) # 85.0

tup.index(92.0) # returns the index of the first occurrence of an element in the tuple
print(tup.index(92.0)) # 2
tup.count(88.5) # returns the number of times an element appears in the tuple
print(tup.count(88.5)) # 1

# IMPORTANT: tup = (1, ) 
tup1 = (1) # this is not a tuple, it is an integer
print(type(tup1)) # <class 'int'>
tup2 = (1, ) # this is a tuple with one element
print(type(tup2)) # <class 'tuple'>

