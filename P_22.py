class me :
    def __init__(self,name,lang):
        self.name=name
        self.lang=lang
        
    def greet(self): #seld parameter
            print(f"I am {self.name} and i love {self.lang}")
            
me1= me("Harshit","Python")
me1.greet()
# print(me1.name,me1.lang)
print(f"I am {me1.name} and i love {me1.lang}") 
