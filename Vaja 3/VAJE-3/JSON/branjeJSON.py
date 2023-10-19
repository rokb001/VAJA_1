import json

person = {
"name" :"Alice",
"age" : 30,
"address": {
    "street":"dunajska",
    "city": "Ljubljana"

},
"married":True

}
with open ("/Users/rb4320/Desktop/VAJA_1/Vaja 3/VAJE/VAJE-3/DATA/POMOC/person.json", "w") as f:
    json.dump(person, f, indent=0, sort_keys=True)