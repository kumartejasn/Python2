#set
# set is an unordered collection of unique elements
# Sets are mutable, meaning you can add or remove items after creation.
# set elements are immutable, meaning you cannot change the value of an element once it is added to the set.
# Sets are defined using curly braces {}
# Sets can store different data types in a single set
# Sets do not allow duplicate members.

s={1,2,3,4,"hello",True,None}
print(s)  # prints the set
 

# adding an item
s.add("tejas")  # adds "tejas" to the set
print(s)  # prints the set with "tejas" added


# deleting an item
s.remove("tejas")  # removes "tejas" from the set
print(s)  # prints the set with "tejas" removed


#pop
s.pop()  # removes a random item from the set
print(s)  # prints the set after removing a random item


#union
# combines two sets and returns a new set with all unique elements from both sets
s2={34,23,1,3,"helo","tejas"}
s3=s2.union(s)
print(s3)  # prints the union of s2 and s, which combines all unique elements from both sets


#intersection
#returns a new set with elements that are common to both sets
s4=s2.intersection(s)  # returns a new set with elements that are common to both sets
print(s4)  # prints the intersection of s2 and s, which contains elements that are present in both sets

#difference
# returns a new set with elements that are in the first set but not in the second set
s5=s2.difference(s)  # returns a new set with elements that are in s2 but not in s
print(s5)  # prints the difference of s2 and s, which contains elements that are in s2 but not in s


#clear
# removes all elements from the set
s5.clear()  # removes all elements from the set
print(s5)  # prints the empty set after clearing it