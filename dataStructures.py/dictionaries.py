# dictionary
#dictionaries are mutable, unordered collections of key-value pairs.
# This file contains functions to manipulate dictionaries in Python.
# Dictionaries are defined using curly braces {}
# Dictionaries are unordered collections of key-value pairs.
# Each key is unique and maps to a value.
# Dictionaries can store different data types in a single dictionary.

D = {
    "name":"dhoni",
    "age":24,
    "team":"india",
    "captain":True
 }

print(D)  # prints the dictionary


#nested dictionary
# A dictionary can contain another dictionary as a value


cricket={
    "team1":"India",
    "captain":"dhoni",
    "players":{
        "batsman":["dhoni","sachin","raina"],
        "bowler":["zaheer","ishant","bumrah"],
        "allrounder":["hardik","jadeja","ashwin"],
        "wicketKeeper":["dhoni","rishabh"]    },

    "board":"BCCI"

}

print(cricket)  # prints the nested dictionary


# dictionary methods

cricket.keys()  # returns a list of all the keys in the dictionary
print(cricket.keys())


cricket.values()  # returns a list of all the values in the dictionary
print(cricket.values( ))


cricket.items()  # returns a list of all the key-value pairs in the dictionary inside tuples
print(cricket.items())


# getting a value by key
cricket["captain"]  # returns the value associated with the key "captain"
print(cricket["captain"])  # prints the value associated with the key "captain"


# adding a new element
cricket["coach"]="rahul dravid"  # adds a new key-value pair to the dictionary
print(cricket)  # prints the updated dictionary with the new key-value pair

# update
cricket.update({"team1":"India"})
# updates the value of the key "team1" to "India"
print(cricket)  # prints the updated dictionary with the new value for "team1"


