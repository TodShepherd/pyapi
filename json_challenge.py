#!/usr/bin/python3

import json

def json_grabber():
    """This function reads in JSON files and returns them"""
    with open("challenge.json", "r") as data:
        datastring = data.read()

    datadecoded = json.loads(datastring)
    
    return datadecoded

def contact_maker(data):

    for element in data:

        friendlist= []

        for friend in element["friends"]:
            friendlist.append(friend["name"])

        print(f"""
        Name: {element['name']}
        Email: {element['email']}
        Phone: {element['phone']}
        Address: {element['address']}
        Friends: {friendlist}""")

def main():
    contact_maker(json_grabber())

if __name__ == "__main__":
    main()

