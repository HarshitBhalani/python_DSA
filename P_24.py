x = []
print(x)
y= [1,2,3,4,5]
print(y)
z= [1,"Hi",3.4,True]
print(z)

w=[9,24,67,239,658]
w.append(10)
print(f"adding 10 in list {w}")

w.sort()
print(f"this is sorted list {w}")

# this is algorotham used to find the lowest value in a list
new_array= [23,45,12,67,34,89,2]
min_value=  new_array[0]

for i in new_array:
    if i<min_value:
        min_value=i
    # print(f"min value is {min_value}") # for undertsnading purpose it is inside loop
print(f"min value is {min_value}") # final min value after loop