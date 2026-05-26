new_list = []
my_list = [10,20,30,40,50]
total = 0
number_count = 0
for i in my_list:
    total += i
    number_count += 1

porcentage = total / number_count

for i in my_list:
    if i > porcentage:
        new_list.append(i)

print("el promedio es de: ", porcentage)
print("los numeros mayores al promedio son: ", new_list)
