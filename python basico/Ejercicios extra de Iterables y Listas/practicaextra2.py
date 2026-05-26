my_list = [1,3,-2,5,7,1,5]

all_positive = True

for i in my_list:
    if i <= 0:
        all_positive = False
        break
if not all_positive:
    print("hay al menos un numero negativo")
else:
    print("todos los numeros son positivos")