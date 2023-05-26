# numbering_placeholder
name = input("enter name : ")
age = int(input("enter age : "))
msg = "Hi {0}, you are {1} years old"
print(msg.format(name, age))


# Naming placeholder
name = input("enter name : ")
age = int(input("enter age : "))
msg = "Hi {name}, you are {age} years old"
print(msg.format(name=name, age=age))
