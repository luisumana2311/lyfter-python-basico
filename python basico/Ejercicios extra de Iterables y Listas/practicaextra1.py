numbers = []
total_counter = 0
while True:
    entrance = input("escriba 10 numeros o fin: ")
    if entrance == ("fin"):
        break
    

    number = int(entrance)
    numbers.append(number)

entrance_search = input("cual numero desea buscar: ")
search =int(entrance_search)

for i in numbers:
    if i == search:
        total_counter += 1


print("del numbero que buscabas hay un total de: " " ",total_counter)

