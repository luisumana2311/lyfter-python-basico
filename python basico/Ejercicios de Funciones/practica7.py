list = [1, 4, 6, 7, 13, 9, 67]
def fun(primos):
    new_list = []
    es_primo = True
    for i in primos:
        es_primo = True
        if i < 2:
            es_primo = False
        else:
            for d in range(2,i):
                if i % d == 0:
                    es_primo = False
                    break
        if  es_primo:
            new_list.append(i)
    return new_list
print(fun(list))

