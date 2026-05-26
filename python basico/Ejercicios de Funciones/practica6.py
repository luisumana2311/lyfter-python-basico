sentence = "python-variable-funcion-computadora-monitor"
list = sentence.split("-")
def fun(order):
    list = order.split("-")
    list.sort()
    result = "-".join(list)
    return result
print(fun(sentence))
