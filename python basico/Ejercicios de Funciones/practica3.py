my_list = [1,2,3,4,6]




def my_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

result = my_numbers(my_list)
print(result)
