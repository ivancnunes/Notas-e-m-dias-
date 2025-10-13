lista_alunos_notas = list()
lista_nome_nota = list()

while True:
    lista_nome_nota.append(input("Informe seu nome: "))
    lista_nome_nota.append(float(input("informe a primeira nota: ")))
    lista_nome_nota.append(float(input("Informe a segunda nota: ")))
    lista_alunos_notas.append(lista_nome_nota[:])
    lista_nome_nota.clear()
    continuar=input("Deseja continuar? (S/N) ").lower()
    if continuar in "n":
        break

print("="*20)
print(f"{"N°":<4}|{"NOME:<10"}|{"MEDIA":>8}")
for index, aluno in enumerate(lista_alunos_notas):
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    media = (nota1+nota2)/2
    print(f"{index:<4} {nome:<10} {media:>8.1f}")
while True:
    notas= int(input("Deseja verificar as notas de algum aluno? (digite 999 para encerrar) "))
    if notas == 999:
        break
    print(f"\nNotas de {lista_alunos_notas[notas][0]} são: {lista_alunos_notas[notas][1], lista_alunos_notas[notas][2]}")