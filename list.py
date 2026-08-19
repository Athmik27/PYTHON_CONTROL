#slicing an list
my_list=['MATHS','SCIENCE',100,200,300]
new_list=my_list[0:2]
print(new_list)

my_list=['MATHS','SCIENCE',100,200,300]
new_list=my_list[0:-2]
print(new_list)

my_list=['MATHS','SCIENCE',100,200,300]
new_list=my_list[:-1]
print(new_list)

my_list=['MATHS','SCIENCE',100,200,300]
new_list=my_list[:-2]
print(new_list)

my_list=['MATHS','SCIENCE',100,200,300]
new_list=my_list[0:]
print(new_list)

#creates an copy of the list
my_list=['MATHS','SCIENCE',100,200,300]
new_list=my_list[:]
print(new_list)

#updating an list
my_list=['MATHS','SCIENCE',100,200,300]
my_list[0]='ENGLISH'
print(my_list)

my_list=['MATHS','SCIENCE',100,200,300]
my_list[-1]='CSE'
print(my_list)

#adding an element to the list this can be done by 2 ways 

#1. append() - adds an element to the end of the list
my_list=['MATHS','SCIENCE',100,200,300]
my_list.append('CIVIL')
print(my_list)

#2. insert() - adds an element at a specific index
my_list=['MATHS','SCIENCE',100,200,300]
my_list.insert(2,'MECHANICAL')     # list.insert(index, value)
print(my_list)

#deleting an element from the list this can be done by 3 ways

#(1) by del keyword
my_list=['MATHS','SCIENCE',100,200,300]
del my_list[-1] 
print(my_list)


#(2) pop keyword
my_list=['MATHS','SCIENCE',100,200,300]
my_list.pop(2)     
print(my_list)



my_list=['MATHS','SCIENCE',100,200,300]
my_list.pop()    # if no index is passed then the last value is removed
print(my_list)



#(3) remove keyword
my_list=['MATHS','SCIENCE',100,200,300]
my_list.remove(200)     
print(my_list)

my_list=['MATHS','SCIENCE',100,200,300]
my_list.remove()  #this gives an error as one argument needs to be passed#   
print(my_list)
