def par_impar(numero):
    if numero % 2 == 0:
        print(numero, "é numero par")
    
    else:
        print(numero, "é numero impar")

numero = int(input("Digite um numero para verificar se ele é par ou impar: "))

par_impar(numero)
