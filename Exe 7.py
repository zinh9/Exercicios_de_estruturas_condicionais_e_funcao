def verifica_quadrante(x, y):
    if x > 0 and y > 0:
        print("O ponto está no primeiro quadrante")
        
    elif x < 0 and y > 0:
        print("O ponto está no segundo quadrante")
        
    elif x < 0 and y < 0:
        print("O ponto está no terceiro quadrante")
        
    elif x > 0 and y < 0:
        print("O ponto está no quarto quadrante")

x = float(input("Digite a coordenada de x: "))
y = float(input("Digite a coordenada de y: "))

verifica_quadrante(x, y)
