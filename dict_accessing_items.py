dict_a = {"name": "raj","age": 25 }
print(dict_a.items())


dict_a = {'name': 'raj','age': 25}
print(dict_a['name'])

dict_a = {'name': 'raj','age': 25}
print(dict_a.get('name'))

"""dict_a = {'name': 'raj','age': 25}  
print(dict_a['city'])"""  # give error

dict_a = {"name": "raj","age": 25 }
print(dict_a.keys())
print(dict_a.values())



dict_a = {"name": "ram", "age": 20}
for key in dict_a.keys():
   print(key)


dict_a = {"name": "ram", "age": 20}
for value in dict_a.values():
   print(value)



# deleting key and value
dict_a = {"name": "ram","age": 20}
del dict_a['age']
print(dict_a)