def verifica(nota):
    if nota >= 7:
        print("Você foi aprovado, parabéns")
    
    else:
        print("Você foi reprovado, se ferrou")

nota = float(input("Digite a sua nota para verificar se você foi aprovado ou reprovado: "))

verifica(nota)
