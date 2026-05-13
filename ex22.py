try: 
    valor = float(input("Digite um valor: "))
    qtd = int(input("Digite a qtd: "))
    tot = valor*qtd
    print("O valor total é: ", tot)
except ValueError:
    print("Algum dos valores está errado")