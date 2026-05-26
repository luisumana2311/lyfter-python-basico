list_words = []
second_list = []
while True:
    words = input("escriba 5 palabras o fin: ")
    if words == "fin":
        break
    list_words.append(words)

for i in list_words:
    if len(i) > 4:
        second_list.append(i)

print("sus palabras fueron: ", list_words)
print("palabras con mas de 4 letras: ", second_list)