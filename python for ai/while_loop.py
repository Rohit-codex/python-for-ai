# while loop 

name = input ("enter your name: ")

while (name == ""):
    print ("you did not enter your name")
    name = input ("enter your name: ")
print (name)

age = int(input("Enter your age: "))

while  (age < 0) :
    print("Invalid input")
    age = int(input("enter your age"))
    
print(age)
                
food = input("Enter a food u like (q to quit): ")
while not food == "q" : 
    print(f"Is this the food you like {food}")
    food = input("Enter a food u like (q to quit): ")
print(food)