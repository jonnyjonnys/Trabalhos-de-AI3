def calculadora():
  while True:
        print("\nOpções:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Ver histórico")
        print("6. Sair")

        escolha = input("Escolha uma operação (1-6): ")

        if escolha == "6":
            print("A sair da calculadora.")
            break
        elif escolha == "5":
            exibir_historico(historico)
        elif escolha in ["1", "2", "3", "4"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                resultado = num1 + num2
                operacao = f"{num1} + {num2} = {resultado}"
            elif escolha == "2":
                resultado = num1 - num2
                operacao = f"{num1} - {num2} = {resultado}"
            elif escolha == "3":
                resultado = num1 * num2
                operacao = f"{num1} * {num2} = {resultado}"
            elif escolha == "4":
                if num2 != 0:
                    resultado = num1 / num2
                    operacao = f"{num1} / {num2} = {resultado}"
                else:
                    operacao = "Erro: Divisão por zero não permitida!"
                    resultado = None
                  
# Executar a calculadora
calculadora()

