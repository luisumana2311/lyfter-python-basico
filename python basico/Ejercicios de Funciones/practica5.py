
sentence = "I love Nación Sushi"
def fun(identificator):
    counter_uppers = 0
    counter_lowers = 0
    for char in identificator:
        if char.isupper():
            counter_uppers += 1
        elif char.islower():
            counter_lowers += 1
    return f"Theres {counter_uppers} upper cases and {counter_lowers} lower cases"
print(fun(sentence))