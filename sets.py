# class set      # create an empty set by set()
my_set={"kumar","vishwa"}
print(type(my_set))

#convert list to set
my_list=["kumar","vishwa"]
my_set=set(my_list)
print(my_set)

##convert dictionary to set
my_dict = {
    'name': 'Athmik',  # in dict we have {key:value}
    'age': 20,
    'course': 'B.Tech'
}
my_set = set(my_dict)
print(my_set)
set(my_dict)          # keys
set(my_dict.keys())   # keys
set(my_dict.values()) # values
set(my_dict.items())  # key-value pairs

#modify an set by add or update method
my_set={"Kumar","John"}
my_set.add(10)# add takes only one argument
print(my_set)

my_set.update({"Jack","Tony"}) #update must be in the format set.update({})
my_set.add(10)
print(my_set)

my_set.update({"Jack","Tony"})
print(my_set)

# deleting an set by remove,dicard,pop,clear method
my_set={"Kumar","John","Tony","Anil"}

my_set.discard("Kumar")#remove and discard takes only one argument
print(my_set)
my_set.remove("Tony")#remove gives an key error if that value is not found in the set.
print(my_set)

my_set.pop()
print(my_set)# pop and clear  take's no argument
my_set.clear()#when used clear() we get an empty set
my_set.discard("Kumar")

print(my_set)
my_set.remove("Tony")

print(my_set)
my_set.pop()
print(my_set)# pop and clear wont take any argument

my_set.clear()
print(my_set)

#set operation
set_1={10,20,30,40,50}
set_2={30,40,50,60,70,80,90}
set_3=set_1.union(set_2)
print(set_3)

set_4=set_1.intersection(set_2)
print(set_4)

set_5=set_1.difference(set_2)
print(set_5)

set_6=set_1.symmetric_difference(set_2)#all the values except the common in both set.
print(set_6)

set_7=set_1.issubset(set_2)#values of set 1 in set 2
print(set_7)

set_8=set_1.issuperset(set_2)#values of set 2 in set 1
print(set_8)

set_9=set_1.isdisjoint(set_2)
print(set_9)








