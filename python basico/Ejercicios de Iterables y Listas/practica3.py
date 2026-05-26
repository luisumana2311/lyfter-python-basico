my_list =["1","2","3","4","5","6","7","8"]

temp = my_list[0]
my_list[0] = my_list [len(my_list) -1]
my_list[len(my_list) - 1] = temp
print(my_list)


