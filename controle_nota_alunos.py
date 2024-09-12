notas = []
while True:
    nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
    
    if nota == -1:
        break
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"Média do aluno: {media:.2f}")

if media >= 7:
    print("Aluno Aprovado!")
elif 5 <= media < 7:
    print("Aluno em Recuperação!")
else:
    print("Aluno Reprovado!")