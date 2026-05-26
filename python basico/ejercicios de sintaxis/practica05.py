total_counter = 0
total_sum = 0

approved_counter = 0
approved_sum = 0

disapproved_counter = 0
disapproved_sum = 0

while True:
    entrance = input("Escriba una nota (0 a 100) o escriba 'fin' para terminar: ")

    if entrance == "fin":
        break

    grade = int(entrance)

    total_sum += grade
    total_counter += 1

    if grade >= 70:
        approved_sum += grade
        approved_counter += 1
    else:
        disapproved_sum += grade
        disapproved_counter += 1


if total_counter > 0:
    average_total = total_sum / total_counter
else:
    average_total = 0

if approved_counter > 0:
    average_passed = approved_sum / approved_counter
else:
    average_passed = 0

if disapproved_counter > 0:
    average_failed = disapproved_sum / disapproved_counter
else:
    average_failed = 0


print("Cantidad de notas aprobadas:", approved_counter)
print("Cantidad de notas desaprobadas:", disapproved_counter)
print("Promedio general:", average_total)
print("Promedio de aprobadas:", average_passed)
print("Promedio de desaprobadas:", average_failed)