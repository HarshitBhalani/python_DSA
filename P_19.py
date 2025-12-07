import json

data = '{"name" : "Harshit","role": "Developer","language": "Python"}'

parseddata = json.loads(data)

print(parseddata["name"])

data1 = { # object
    "name" : "Harshit",
    "role": "Developer",
    "language": "Python",
    "modules": ["Python", "Django", "Flask"], # array
    "cars": [
    {"model": "BMW m5", "High speed": 300},
    {"model": "macleran", "High speed": 350}
  ]
}

#convert into json
jsondata = json.dumps(data1)
print(jsondata) #give json string

#use 4 indents to make it easier to read
print(json.dumps(data1, indent=4))