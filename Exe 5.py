def triangulo(lado_1, lado_2, lado_3):
    if lado_1 == lado_2 and lado_2 == lado_3:
        print("O triangulo é equilatero")
    
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("O triangulo é isósceles")
    
    else:
        print("O triangulo é escaleno")

lado_1 = float(input("Digite o primeiro lado do triangulo: "))
lado_2 = float(input("Digite o segundo lado do triangulo: "))
lado_3 = float(input("Digite o terceiro lado do triangulo: "))

triangulo(lado_1, lado_2, lado_3)
