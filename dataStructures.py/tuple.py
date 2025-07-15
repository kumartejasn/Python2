# tuple 
# tuples are immutable sequences in Python, used to store multiple items in a single variable.
# Tuples are ordered and allow duplicate members.
# Tuples can store different data types in a single tuple
# Tuples are defined using parentheses ()

T=(1,2,3,4,"hello", True, None, 5)
t1=(1,) # this is a tuple with one item, note the comma

print(T)
print(t1)  # prints the tuple with one item
print(type(T))  # prints the type of T, which is <class 'tuple'>


# slicing
# returns a tuple containing the specified range of items

print(T[1:3])
print(T[-3:-1])  # returns elements from third last to second last (last is not included)
print(T[ :4])  # returns elements from start to index 3 (4 is not included)
print(T[2:])  # returns elements from index 2 to the end of the tuple



# count
# returns the number of occurrences of a specified item in the tuple  


c=(1,2,3,4,4,1,2,3,4,"hello", True, None, 5)
print(c.count(3))  # counts how many times 3 appears in the tuple
print(c.count(4))  # counts how many times 4 appears in the tuple

# sort
# tuples cannot be sorted in place, but you can convert them to a list, sort the list, and then convert it back to a tuple