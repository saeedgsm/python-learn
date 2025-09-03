thislist = ["apple", "banana", "cherry"]
print(thislist)

print("Length of list : ",len(thislist))

print("type of list : ",type(thislist))

thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")) # note the double round-brackets
print(thislist)

# Access Items
print("access items : ",thislist[2])

# Negative Indexing
print("Negative Indexing : ",thislist[-3])

# Range of Indexes
print("Range of Indexes : ",thislist[1:-1])

print(thislist[:4])

# Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change Item Value
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist[1:2] = ["blackcurrant", "watermelon","melon", "mango"]

print(thislist)


# Insert Items
thislist.insert(2, "watermelon")
print(thislist)

#  Add List Items
thislist.append("orange")
print(thislist)


# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist,type(thistuple))