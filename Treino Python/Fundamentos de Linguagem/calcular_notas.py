def calcular_notas():
    
    nome = input("Qual o nome do aluno?: ")

    try:
        nota1 = float(input("Digite a primeira nota (0-10): "))
        nota2 = float(input("Digite a segunda nota (0-10): "))
        nota3 = float(input("Digite a terceira nota (0-10): "))

        if not all(0 <= n <= 10 for n in [nota1, nota2, nota3]):
            print("Erro: As notas devem ser entre 0 e 10.")
            return

        notas = [nota1, nota2, nota3]
        media = sum(notas) / len(notas)

        if media >= 7.0:
            situacao = "Aprovado"
        elif media >= 4.0:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        print(f"\n--- Resultado Final ---")
        print(f"Aluno: {nome}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print(f"-----------------------")

    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")


calcular_notas()
