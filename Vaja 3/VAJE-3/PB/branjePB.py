import person_pb2

person=person_pb2.Person()

with open ("C:/Users/rb4320/Desktop/VAJA_1/Vaja 3/VAJE-3/PB/person_pb2.py","rb") as f:
    person.ParseFromString(f.read())

person.age=31
person.married=False

with open("C:/Users/rb4320/Desktop/VAJA_1/Vaja 3/VAJE-3/DATA/POMOC/person_updated.pb") as f:
    f.write(person.SerializeToString())

    print(person)