#jeanca ignore mis apuntes este me costo mucho y mejor apunto para el futuro
numbers = []

while True:
    entrance = input("escriba 10 numeros y luego escriba fin: ")

    if entrance == "fin":
        break

    number = int(entrance)
    numbers.append(number)#mete el ultimo valor ala lista

max_value = 0

for i in numbers:
    if i > max_value:#Para cada número de la lista,si ese número es mayor que el máximo que llevo,entonces guardalo como el nuevo máximo
        max_value = i

print("Max value:", max_value)