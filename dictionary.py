#this stores data in {key:value} pair
student = {
    "name": "Athmik",
    "age": 20,
    "branch": "CSE"
}
print(student["name"])
print(student["age"])

#use of get()
print(student.get("name"))

#update
student["college"] = "ABC College"

#delete
student.pop("age")
del student["branch"]#del deletes the item but doesn't return it. pop() removes and returns the value. so we use [] for dwlwte and () for pop.

#getting an key
print(student.keys())

#getting an value
print(student.values())

#getting an item
print(student.items())

#loop through dictionary
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for item in student.items():
    print(item)

# #operations on dictionary
# Create this dictionary:
# name = Raju
# age = 21
# city = Udupi
# Then print the name and city using dictionary keys.
#add/update age
#remove an age
Student={
     "name": "Raju",
     "age": 21,
     "city": "Udupi"
}
print(Student["name"])
print(Student["city"])

Student["age"]=25
print(Student["age"])

Student.pop("age")#removes the value and do not returns
del Student["city"]#removes the value and do not return it 
Student.clear()#removes everything

#check using "in"
print("name" in Student)
print("marks" in Student)

#check using 'if'
if "age" in Student:
    print("Age exists")

