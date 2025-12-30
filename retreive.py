import json

with open("address.json", "r") as file:
    data = json.load(file)

for addr in data["addresses"]:
    if addr["type"] == "home":
        print(" ")
        print(addr["street"])
        print(addr["city"], addr["state"], addr["zip"])

    if addr["type"] == "school":
        print(" ")
        print(addr["street"])
        print(addr["city"], addr["state"], addr["zip"])