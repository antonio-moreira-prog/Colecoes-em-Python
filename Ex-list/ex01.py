# Crie um algoritmo que armazene quatro notas em uma lista e que apresente:
# Média final,
# Maior nota,
# Menor nota;
notas = []

while True:
    num_notas = input("Quantas notas você quer inserir na lista? (digite 'sair' para finalizar): ")

    if num_notas.lower() == "sair":
        break

    try:
        num_notas = int(num_notas)
    except ValueError:
        print("Por favor, insira um valor válido.")
        continue
 
    for i in range(num_notas):
        while True:
            try:
                nota = float(input(f"Informe a {i+1}ª nota: "))
                break
            except ValueError:
                print("Por favor, insira um valor número.")

        notas.append(nota)

    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / len(notas)

    print(f"\nMédia final: {media:.2f}")
    print(f"Maior nota: {maior_nota:.2f}")
    print(f"Menor nota: {menor_nota:.2f}\n")

# print(type(notas))