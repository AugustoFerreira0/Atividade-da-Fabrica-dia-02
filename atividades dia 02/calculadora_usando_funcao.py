def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

def calc():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite 1/2/3/4: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", soma(num1, num2))
    elif escolha == '2':
        print("Resultado:", sub(num1, num2))
    elif escolha == '3':
        print(f"Resultado:", multi(num1, num2))
    elif escolha == '4':
        print("Resultado:", divi(num1, num2))
    else:
        print("Escolha inválida.")

