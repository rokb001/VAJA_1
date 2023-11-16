import requests
import json

node_url = "https://mainnet.infura.io/v3/8891db36a05f485486fd7979445d5611"

payload = {

        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ["latest",True],
        "id": 0
}

header = {
    "Content-Type":"application/json"
}
response = requests.post(node_url,data=json.dumps(payload),headers=header)


if response.status_code == 200:
    print("dobili smo blok")
    with open("blockData.json","w") as f:
        json.dump(response.json(),f,indent=4)

else:{
        print("ni ratal, error code:"+ response.text)

    }

def counter():
data=block_data.copy()


def izlusciNaslove(blockNum="latest"):
data = getBlock(blockNum).copy()

podatki = dict(od =[], to=[])
    print(counter(data))


def main():
    print(f"zadnji blok:{getBlock()}")
    print("st trensakcij: {preste}Transakcije()")
    #for transaction in data["result"]["transaction"]:

    

# definiraj VARIABLE nase skripte
    # API URL od infure za Ethereum mainnet


    # JSON-RPC request payload  (pogledamo dokumentacijo!)


    # Nastavimo headerje za JSON-RPC request


# Pošljemo request (uporabimo requests.post mdetodo)


# Error handling. POgledamo če smo dobili pravilen odgovor.
    # ce ni error-ja (status code 200) sprintamo sporocilo in shranimo dobljeno sporocilo v json

    # else, sprintaj sporocilo da nam ni uspelo dobiti zadnji block in dodaj kateri error oz. code-status code smo dobili