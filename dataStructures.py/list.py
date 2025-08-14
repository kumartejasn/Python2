# # lists are a collection of items that are ordered and changeable.
# # Lists allow duplicate members.
# # can store different data types in a single list

# l=[1,2,3,6,2,4,"hello",True, None]
# # Lists are defined using square brackets []
# print(l)



# # functions or methods that can be used with lists

# # slicing 

# s=[2,3,6,2,4,"hello",True]
# print(s[2:4])  # returns elements from index 2 to index 3 (4 is not included)
# print(s)

# print(s[-2:-1])  # returns elements from second last to last (last is not included)



# # append 
# # adds an item to the end of the list
# A=["a","f",2,3,4,True]
# print(A)
# A.append("g")
# print(A)  # now A has "g" at the end



# # insert
# # adds an item at a specified index
# i=[2,3,6,2,4,"hello",True]
# i.insert(1,None)  # this will add None at index 1
# print(i)  # now i has None at index 1

# #remove
# # removes the first occurrence of a specified item
# r=[2,3,6,2,4,"hello",True]
# r.remove(6)  # this will remove the first occurrence of 6
# print(r)  # now r has no 6 in it

# #pop
# # removes the item at the specified index and returns it
# p=[2,3,6,2,4,"hello",True]
# p.pop(3) # this will remove the item at index 3 (which is 2)
# print(p)  # now p has no 2 at index 3
# print(p.pop())  # this will remove the last item (True) and return it

# # reverse
# # reverses the order of the list
# rev=[2,3,6,2,4,"hello",True]
# rev.reverse() # this will reverse the order of the list
# print(rev)  # now rev is in reverse order

# # sort
# # sorts the list in ascending order
# so =[2,5,1,5,5,0,4,1]
# so.sort()  # this will sort the list in ascending order
# print(so)



def multiply(numbers):
    total=1
    for i in numbers:
        total *= i
    print(total)
    return total
multiply([5,3,6,7])
print(multiply([1,2,3,4,5]))  