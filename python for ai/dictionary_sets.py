# # 100 day Revision of Python 
# day 5: Dictionary and sets 
# Dictinoary 
collection = { 
    "name" : "alex",
    "cgpa" : 9.45,
    "marks" : [8,9,7.5],
    "is_adult" : True,
    "subjects" : [ "py" , "c" , "java"],
    "topics" : (1,2,3)
} 
print(collection["name"])
print(collection["topics"])
collection["name"] = "alex"
collection["name"] = "alexa"
print(collection) # mutable
Nested dictionary 
student = {
    "name" : "rahlu kumar",
    "subjects" : {
        "phy" : 25,
        "chem" : 28,
        "math" : 30,
    }
} 
print(student ["subjects"] ["chem"])
print(len(student))
print(list(student.keys()))
print (student.values())
print (student.items()) #returns vlues as tuples 
pairs=list(student.items())
print(pairs[1])
print(student["name2"]) #error
print(student.get("name2")) #no error
student.update({"city": "delhi"})
print(student)
    
Sets in Python
duplicate elements not allowed in sets
collection = {1 ,2 ,2 ,4 , "hello", "world"} 

print(collection)
print(type(collection))
print(len(collection))
collection = set() #empty set
print(type(collection))
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("alex")
collection.add((1,2,3))
collection.add((1,2,3))
collection.clear()
print(collection.pop())
print(collection.pop())
set1 = {1,2,3}
set2 = {1,2,4}

print(set1.union(set2)) #{1,2,3,4}
print(set1.intersection(set2)) #{1,2}