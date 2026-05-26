list_of_keys = ["acces_level", "role"]
employe = {"name": "john", "email": "john@ecorp.com", "acces_level": 5, "age": 28}
employe.pop("age")
employe.pop("acces_level")
print(employe)