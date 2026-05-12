# 100 day Revision of Python 
# day 2: Strings
# String is a sequence of characters enclosed in single quotes, double quotes or triple quotes
str1 = 'Hello World!' # using single quotes
str2 = "Hello World!" # using double quotes
str3 = """Hello World!""" # using triple quotes    
print(str1)
print(str2) 
print(str3)
# String concatenation
str4 = str1 + " " + str2
print(str4)

# String operations
print("Length of str1: ", len(str1)) # 12
print("str1 in uppercase: ", str1.upper()) # HELLO WORLD!
print("str1 in lowercase: ", str1.lower()) # hello world!

# String indexing and slicing
str5 = "Vellore Institute of Technology"
str6 = "vellore institute of technology"
print("First character of str5: ", str5[0]) # V
print("Last character of str5: ", str5[-1]) # y
#slicing
print("Substring of str5 from index 0 to 6: ", str5[0:7]) # Vellore       # LAST INDEX IS EXCLUDED
print("Substring of str5 from index 11 to 20: ", str5[11:21]) #  titute of 
print("Substring of str5 from index 21 to end: ", str5[21:]) #   Technology
print("Substring of str5 from start to index 10: ", str5[:11]) # Vellore Ins

# String Functions
print("Number of times 'o' appears in str5: ", str5.count('o')) # 3
print("Index of first occurrence of 'o' in str5: ", str5.find('o')) # 4
print(str5.endswith("Technology")) # True
print(str6.capitalize()) # Vellore institute of technology
print(str6.title()) # Vellore Institute Of Technology
print(str6.replace("vellore", "Vellore")) # Vellore institute of technology



