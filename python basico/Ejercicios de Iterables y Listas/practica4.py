my_list = [1,2,3,4,5,6,7,8,9]
pairs =[]
for number in my_list: #esto toma uno por uno en mi lista
    if number % 2 == 0: #esto te dice cuales son los numeros pares
        pairs.append(number)# esto pregunta si el numero es par y lo mete en la lista
        print(pairs)