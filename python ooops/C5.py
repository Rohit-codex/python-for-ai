# Q1 
Dictionary={
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "small animal"
} 
print(Dictionary)

#Q2
Subjects = {
    "p","j","c++","p","js","j","p","j","c++","c"
    }
print(len(Subjects))

#Q3
dict = {
    "subject" : {
        "phy" : 25,
        "chem" : 28,
        "math" : 30,

    }
} 
print(dict)
     #or
marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

print(marks)

#Q4
number = set()
number.add(9)
number.add("9.0")        
print(number)
    
       #or

number = {
    ("float" , 9.0),
    ("int" , 9)
}
print(number)
