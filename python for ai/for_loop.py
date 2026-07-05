# Revision of python 
# for loop 

for x in range (1 , 11):
    print(x) 

for x in range (1 , 11, 2):
      print(x) 

# reversed for loop 

for x in reversed (range (1 , 11)):
    print(x) 


# for loop (string)

credit_card = "1234-56789"

for x in credit_card:
    print(x)

# Break and  Continue

for x in range(1, 21):
    if x == 13:
        continue # (13 skipped )
    else:
         print(x)

for x in range(1, 21):
    if x == 13:
        break # ( stop before 13)
    else:
         print(x)          