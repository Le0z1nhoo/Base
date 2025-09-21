print("Seja Bem Vindo(a) à Calculadora! :)")
number = float(input("Digite um número: "))
number1 = float(input("Digite mais um número: "))
operacao = input("Escolha a Operação (+, -, *, /): ")
if operacao == "+":
    print(f"A soma dos números é {number + number1}")
elif operacao == "-":
    print(f"A subtração dos números é {number - number1}")
elif operacao == "*":
    print(f"A multiplicação dos números é {number * number1}")
elif operacao == "/":
    if number1 == 0:
        print("Não é possível dividir por zero.")
    else:
        print(f"A divisão dos números é {number / number1}")
else:
    print("Opção inválida!")