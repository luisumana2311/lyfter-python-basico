number1 = int(input("ingrese el primer numero: "))
number2 = int(input("ingrese el segundo numero: "))
number3 = int(input("ingrese el tercer numero: "))
if (number1 > number2) and (number1 > number3):
    print(f"el primer numero es el mayor {number1}")
elif (number2 > number1) and (number2 > number3):
    print(f"el segundo numero es el mayor {number2}")
else:
    print(f"el tercer numero es el mayor {number3}")