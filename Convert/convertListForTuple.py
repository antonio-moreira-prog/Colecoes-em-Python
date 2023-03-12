lista = []

lista.append("Ana")
lista.append("Antonio")
lista.append("Maria")
lista.append(False)
lista.append(42)
lista.append(3.14)

print(lista)
print("*" * 25)

NovaTupla = tuple(lista)  # convertendo a lista em uma tupla
print(NovaTupla)

print(type(NovaTupla))

