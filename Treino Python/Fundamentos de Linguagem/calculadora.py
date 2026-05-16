def calculadora():
    print("Selecione uma opção:")
    print("1: Adição(+)")
    print("2: Subtração(-)")
    print("3: Multiplicação(*)")
    print("4: Divisão(/)")

    escolha = input("Digite a opção (1/2/3/4): ")

    if escolha in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite números.")
            return
        
        match(escolha):
            case "1":
                print(f"A soma dos números é: {num1 + num2}")
            case "2":
                print(f"A subtração dos números é: {num1 - num2}")
            case "3":
                print(f"A multiplicação dos números é: {num1 * num2}")
            case "4":
                try:
                    print(f"A divisão dos números é: {num1 / num2}")
                except ZeroDivisionError as error:
                    print(error)
    else:
        print("Opção inválida!")

calculadora()