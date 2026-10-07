def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b


def calculadora():
    print("=== CALCULADORA SIMPLES ===")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")

    while True:
        opcao = input("\nEscolha uma opção (1-5): ").strip()

        if opcao == '5':
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao not in ['1', '2', '3', '4']:
            print("Opção inválida! Escolha um número de 1 a 5.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
            continue

        if opcao == '1':
            resultado = somar(num1, num2)
            simbolo = "+"
        elif opcao == '2':
            resultado = subtrair(num1, num2)
            simbolo = "-"
        elif opcao == '3':
            resultado = multiplicar(num1, num2)
            simbolo = "*"
        elif opcao == '4':
            resultado = dividir(num1, num2)
            simbolo = "/"

        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"Resultado: {num1} {simbolo} {num2} = {resultado}")


if __name__ == "__main__":
    calculadora()