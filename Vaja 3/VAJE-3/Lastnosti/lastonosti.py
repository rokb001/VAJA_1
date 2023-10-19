import os
import json

with open (r"C:\Users\rb4320\Desktop\VAJA_1\Vaja 3\VAJE-3\DATA\POMOC\person.json", "r") as f:
    data = json.load(f)

for key, value in data.items():
    print (f"{key}: {type(value)}")

    print("se za PB message fiels!")

person_pb = Person ()

with open (r"C:\Users\rb4320\Desktop\VAJA_1\Vaja 3\VAJE-3\DATA\POMOC\person.pb","rb") as f:

    person_pb.ParseFromString(f.read())


    for field,value in person_pb.ListFields():
        print(f"Field: {field.name}, Type: {field.type}, Value: {value}")
