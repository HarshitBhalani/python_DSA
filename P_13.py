a=300
b=400

if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")

    
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")


day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
  
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("not above 20.")
    
age=21
licence=True 
if age>=18 and licence:
    print("You can drive")
else:
    print("You cannot drive")


score = 85
attendance = 90
submitted = True
if score >= 80 and attendance >= 75 and submitted:
    print("You passed the course!")
    if score>=90:
        print("With Distinction!")
        if attendance==100:
            print("good attendance")
            if submitted:
                print("done")
                if not submitted:
                    print("not done")