name = input("¿Cuál es tu nombre? ")
lastname = input("cual es tu apellido? ")
age = int(input("cual es tu edad?"))
if (age >55):
    print(f"{name} {lastname}" " "+ f"usted es un adulto mayor de {age} años")
elif(age>= 27):
    print(f"{name} {lastname}" " "+ f"usted es un adulto de {age} años")
elif(age>= 18):
    print(f"{name} {lastname}" " "+ f"usted es un adulto joven de {age} años")
elif (age >= 11):
    print(f"{name} {lastname}" " "+ f"usted es un adoslecente de {age} años")
elif(age >= 4):
    print(f"{name} {lastname}" " "+ f"usted es un niño de {age} años")
elif(age<= 4):
    print(f"{name} {lastname}" " "+ f"usted es un bebe de {age} años ")
