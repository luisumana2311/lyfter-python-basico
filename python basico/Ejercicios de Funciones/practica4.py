sentence = "hola mundo"

def fun(reorder):
    new = ""
    for i in range(len(reorder)-1,-1,-1):
        new += reorder[i]
    return new

print(fun(sentence))

