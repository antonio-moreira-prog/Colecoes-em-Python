lista = [] 

# 1. Add elementos
# 1.1 append()
lista.append("Ana")
lista.append("Antonio")
lista.append("Maria")
lista.append(False)
lista.append(42)
lista.append(3.14)

# 1.2 extend()
lista.extend([34, 345, 87])

# 1.3. insert()
lista.insert(0, 2)

# 2. Remover
# 2.1 remove()
lista.remove("Antonio")

# 2.2 pop()
lista.pop(0)

# 2.3 pop()
# lista.clear()

# 2.4 del
del lista[2]

# 3 Procurando elementos na lista
print("*" * 10 + " Procurando elementos na lista " + "*" * 10)

# 3.1 index()
print(lista.index(42))

# 3.2 count()
print(lista.count(87))

print("*" * 10 + " imprimindo lista " + "*" * 10)
print(lista)

print("*" * 10 + " Elementos pelo index 2 " + "*" * 10)
print(lista[0])
print(lista[2])

print("*" * 10 + " Iterando uma lista " + "*" * 10)
for elemento in lista:
    print(elemento)

# 4 Copiando a lista
nova_lista = lista.copy()

print("*" * 10 + " Nova lista " + "*" * 10)
import random
lista_aleatoria = []
for i in range(10):
    lista_aleatoria.append(random.randint(1, 10))
print(lista_aleatoria)

# 5 Ordenando a lista
print("*" * 10 + " Ordenando a nova lista " + "*" * 10)
lista_aleatoria.sort(reverse=False)
print(lista_aleatoria)

# print(type(lista))




