dict = {
    "car" : "BMW m5",
    "year" : 2004,
    "color": "blue"
}

print(dict.items())

print(dict["color"])

dict["model"] = "ford"
print(dict)

dict.pop("year")