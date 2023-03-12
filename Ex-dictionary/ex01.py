dicionario_time = {}

dicionario_time["Time"] = "Corinthians"
dicionario_time["Patrocínio"] = "Nike"
dicionario_time["Estádio"] = "Neo Química"

print(dicionario_time["Time"])
print(dicionario_time["Patrocínio"])
print(dicionario_time["Estádio"])

print("*" * 25)

dicionario_time["Patrocínio"] = "Banco BMG"
print(dicionario_time["Patrocínio"])

del dicionario_time["Estádio"]
print(dicionario_time) # saída: {"Time": "Corinthians", "Patrocínio": "Banco BMG"}