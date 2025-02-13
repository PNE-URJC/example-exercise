#!/usr/bin/python3
""" This program parses a file with library information and dumps it """
#
# This program parses files with content like this one:
#
# Library Name;Address;Postal Code;City;Country;Telephone
# books: The Odissey;The Iliad;
# cds: Smeels Like Teen Spirit; The Wall;
# maps: Spain, Italy
#
# The program reads previous file and dumps the library information:
# library_name, address, postal_code, city, country
#
# Apart from that, it creates a dictionary with the following structure:
# books: ['The Odissey', 'The Iliad']
# cds: ['Smeels Like Teen Spirit', 'The Wall']
# maps: ['Spain', 'Italy']
#
# Apart from that, the program will allow to locate a specific value in the dictionary by key:
# locate("cds", "The Wall") -> True
# locate("cds", "Money") -> False

from pathlib import Path

# -- Constant with the name of file to open
FILENAME = "library.txt"
library = {
        "books": [],
        "cds": [],
        "maps": []
}

def parse_file(file_name):
    """ Function to parse the file and dump the library information """
    file_contents = Path(file_name).read_text()
    lines = file_contents.split("\n")
    library_name, address, postal_code, city, country, telephone = lines[0].split(";")
    library_name = library_name.strip()
    address = address.strip()
    postal_code = postal_code.strip()
    city = city.strip()
    country = country.strip()
    print("Library Information:")
    print(f"Name: {library_name}\nAddress: {address}\nPostal Code: {postal_code}")
    print(f"City: {city}\nCountry: {country}\nTelephone: {telephone}")

    for line in lines[1:]:
        if line:
            line_list = line.split(":")
            key = line_list[0]
            values = line_list[1]
            values = values.strip().split(";")
            library[key].extend(values)
    print("Library:", library)

def locate(key, value):
    """ Locate a value in the library dictionary """
    if key in library:
        if value in library[key]:
            print(f"Found {value} in {key}")
            return True
    return False

if __name__ == "__main__":
    parse_file(FILENAME)
    print("Locate cds: The Wall:", locate("cds", "The Wall"))
    print("Locate cds: Money:", locate("cds", "Money"))
