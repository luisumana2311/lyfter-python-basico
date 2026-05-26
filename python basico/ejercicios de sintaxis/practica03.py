import random
secret_number = random.randint(1, 10)
while True:
    respuesta = int(input("escriba un numero del 1 al 10: "))

    if respuesta == secret_number:
        print("felicidades, adivinaste el numero secreto")
        break
    else:
        print("te has equivocado")