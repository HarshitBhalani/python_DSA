import re
from Modules import P_20_module

x= re.search("Harshit", P_20_module.txt["text"])

if x :
    print(f"Found") #group() method is used to get the actual matched string  ::  code-> x.group()
else : 
    print(f"not found {x}")