# example-exercise

This program parses files with content like this one:

Library Name;Address;Postal Code;City;Country;Telephone
books: The Odissey;The Iliad;
cds: Smeels Like Teen Spirit; The Wall;
maps: Spain, Italy

The program reads previous file and dumps the library information:
library_name, address, postal_code, city, country

Apart from that, it creates a dictionary with the following structure:
```python
books: ['The Odissey', 'The Iliad']
cds: ['Smeels Like Teen Spirit', 'The Wall']
maps: ['Spain', 'Italy']
```

Apart from that, the program will allow to locate a specific value in the dictionary by key:
```python
locate("cds", "The Wall") -> True
locate("cds", "Money") -> False
```
