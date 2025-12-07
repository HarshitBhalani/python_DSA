def myfuc(fname): #fname is parameter 
    print("Hello " + fname)

myfuc("Harshit") #this is an arg

    
def myfunc1():
  x = "Harshit"
  def myfunc2():
    nonlocal x
    x = "python"
  myfunc2()
  return x

print(myfunc1())

def countdown(n):
    if (n<=0):
        print("done")
    else : 
        print(n)
        countdown(n-1)
countdown(5)

