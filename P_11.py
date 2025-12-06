fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

list1 = ["apple", "banana", "cherry"]
list1.append("orange")  # can use insert() to add at specific position
list1.insert(1, "grapes")
list1.remove("banana")  # use pop() to remove also
list1.sort()
list1.reverse()
print(list1)

print(list1)



for x in list1:
    print(x)