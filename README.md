"""
Calculadora simples em Python.

Este programa apresenta um menu de operações matemáticas e permite ao
usuário realizar soma, subtração, multiplicação e divisão.

A estrutura do programa foi organizada em funções para separar cada
operação e facilitar a leitura, manutenção e reutilização do código.

Como executar pelo arquivo .sh
------------------------------
1. Certifique-se de que os arquivos `iniciar.sh` e
   `calculadora_documentada.py` estejam na mesma pasta.
2. No terminal, acesse essa pasta.
3. Dê permissão de execução ao inicializador com:

       chmod +x iniciar.sh

4. Execute o inicializador com:

       ./iniciar.sh

O arquivo `iniciar.sh` chama o interpretador Python 3 e executa
`calculadora_documentada.py`.
"""


def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração do segundo número pelo primeiro."""
    return a - b


def multiplicar(a, b):
    """Retorna o resultado da multiplicação de dois números."""
    return a * b


def dividir(a, b):
    """
    Divide o primeiro número pelo segundo.

    Antes da divisão, verifica se o segundo número é zero. Essa
    verificação evita um erro de divisão por zero e retorna uma
    mensagem explicativa ao usuário.
    """
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b


def calculadora():
    """
    Executa a calculadora e controla a interação com o usuário.

    O programa:
    1. Exibe um menu com as operações disponíveis.
    2. Solicita ao usuário uma opção de 1 a 5.
    3. Encerra quando a opção 5 é escolhida.
    4. Valida a opção informada.
    5. Solicita dois números e trata entradas que não sejam numéricas.
    6. Executa a operação escolhida.
    7. Exibe o resultado na tela.

    O laço while mantém a calculadora funcionando até que o usuário
    escolha a opção de saída.
    """
    print("=== CALCULADORA SIMPLES ===")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")

    while True:
        # Solicita a opção e remove espaços desnecessários da entrada.
        opcao = input("\nEscolha uma opção (1-5): ").strip()

        # A opção 5 encerra o programa.
        if opcao == '5':
            print("Encerrando a calculadora. Até mais!")
            break

        # Verifica se a opção escolhida corresponde a uma operação válida.
        if opcao not in ['1', '2', '3', '4']:
            print("Opção inválida! Escolha um número de 1 a 5.")
            continue

        # Tenta converter as entradas para números decimais.
        # Se o usuário digitar texto, ValueError será tratado.
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
            continue

        # Seleciona a função correspondente à opção escolhida.
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

        # A divisão por zero retorna uma mensagem (string), que é exibida
        # diretamente. Nos demais casos, o resultado é um número.
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"Resultado: {num1} {simbolo} {num2} = {resultado}")


# Garante que a calculadora seja executada somente quando este arquivo
# for iniciado diretamente, e não quando for importado por outro programa.
if __name__ == "__main__":
    calculadora()
