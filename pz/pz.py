# import random 

# jackport = random.randint(1,100)
# guess = int(input("kar guess: "))

# while guess != jackport:
#     if guess < jackport : 
#         print ("gaalt guess higher: ")
    
#     else :
#         print("galat guess lower")
#     guess = int(input("guess again: "))

# print(f"Congo {guess} is right ")    
    
rows = int(input("n = "))

for i in range (1, rows):
    for j in range (1,i):
        print (j, end=" ")

    print()    
    