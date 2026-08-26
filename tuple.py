#tuple is immutable list ao it do not support the operations that list do.
tuple=(10,20,30,"Athmik")
#indexing
print(tuple[3])

#slicing
tuple=(10,20,30,40,50,60,70,80)
print(tuple[0:4])
print(tuple[0:])
print(tuple[:])

#counting
tuple=(1,3,3,3,5,6,7,8,8,9)
print(tuple.count(3))
print(tuple.count(1))

#getting an index of an value
tuple=("Kumar","Raju",10,20)
print(tuple.index(10)) #this gives the index of an value
print(tuple[0:3]) #this gives an value of the index

#cmp(tuple_1,tuple_2)
#max(tuple_1)
#min(tuple_1)
#len(tuple_1)
#tuple(seq) coverts tuple to list
