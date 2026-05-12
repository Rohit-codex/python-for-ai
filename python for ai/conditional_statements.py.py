# 100 day Revision of Python 
# day 3: Conditional Statements
# Conditional statements are used to perform different actions based on different conditions.
# 
# if statement

x = 100
num = int(input("Enter a number: "))
if x > num:
    print("x is greater than num") 

# if-else statement
if x > num:
    print("x is greater than num")
else:
    print("x is not greater than num")

# if-elif-else statement
if x > num:
    print("x is greater than num") 
elif x == num:
    print("x is equal to num")  
else:    
    print("x is less than num")