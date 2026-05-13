try:
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))
    result = num1+num2
    print("O resultado é: ", result)
except ValueError:
    print("Digite apenas números")