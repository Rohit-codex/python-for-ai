#simple calculator program
operator = input("enter your operator + - * / : ")
num1 = float(input("enter num : "))
num2 = float(input("enter num : "))

if ( operator == "+" ) :
    result = num1+num2
    print(result)

elif (operator == "-" ) :
    result = num1-num2
    print (result)

elif (operator == "*" ) :
    result = num1*num2
    print (result)

elif (operator == "/" ) :
    if (num2 == 0):
        print("invalid request")
    result = num1/num2
    print (result)
else:
    print("operator not found")

# Simple weight conversion program
#kilo to pounds or pounds to kilo

weight =  float (input("enter your weight: "))
unit = input("kilogram or Pound? (K or L) : ")

if ( unit == "K"):
    weight = weight*2.205
    print(weight)
elif ( unit == "L" ) :
    weight = weight/2.205
    print(weight)
else:
    print("invalid category")  

# temperature conversion 
# celcius to kelvin and kelvin to celcius
    
temperature = float (input("enter temperature: "))
unit = input("celcius or pound (C or K): ")

if (unit == "C"):
    temperature = temperature + 273
    print(round(temperature))
elif (unit == "K"):
    temperature = 273 - temperature    
    print(round(temperature))
else : 
    print("Invalid request")