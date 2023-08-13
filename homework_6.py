import json
t=open('dictionary.json')
data=json.load(t)
data_input=input("Enter The world: ")
data_input.lower()

try:
    data
    print(data[data_input])
except:
    print("error\nthe world is unavailable ")