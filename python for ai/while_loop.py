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

num = int(input("enter a number: "))

while num < 1 or num > 10 : 
    print (f"Not Valid number:{num}")
    num = int(input("enter a number: "))
print(num) 

# Interest calculator 

principle = 0                                           
rate = 0
while principle <= 0:
    principle = float(input("enter the principle : "))
    if principle <= 0:
        print("not valid")

while rate <= 0:
    rate = float(input("enter the rate : "))
    if rate <= 0:
        print("not valid")

while time <= 0:
    time = int(input("enter the time in years : "))
    if time <= 0:
        print("not valid")     

# or including 0 

principle = 0
time = 0 
rate = 0
while True:
    principle = float(input("enter the principle : "))
    if principle < 0:
        print("not valid")
    else :
        break    

while True:
    rate = float(input("enter the rate : "))
    if rate < 0:
        print("not valid")
    else :
        break    


while True:
    time = int(input("enter the time in years : "))
    if time < 0:
        print("not valid") 
    else :
        break    
           

total = principle * pow((1 + rate / 100),  time)
print(f"${total:.2f}")
