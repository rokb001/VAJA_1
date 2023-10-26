import json

pot = 'C:/Users/RogStrix/Source/Repos/VAJA_1/Vaja 3/zacetniData.json'

with open(pot,'r') as file:
   zacetniData = json.load(file)


pot2 = 'C:/Users/RogStrix/Source/Repos/VAJA_1/Vaja 3/updateData.json'

with open(pot2,'r') as file2:
   updateData = json.load(file2)
   
zacetnislovar = dict (zacetniData)

