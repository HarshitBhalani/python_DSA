import os
with open("C:\\Users\\HARSHIT\\Desktop\\DSA\\files\\P_23_file.txt", "a") as f:
  f.write("more content added")

#open and read the file after the appending:
with open("C:\\Users\\HARSHIT\\Desktop\\DSA\\files\\P_23_file.txt") as f:
  print(f.read())

# x crates file
# f = open("myfile.txt", "x")
# myfile,txt created


os.remove("myfile.txt")
# myfile.txt deleted