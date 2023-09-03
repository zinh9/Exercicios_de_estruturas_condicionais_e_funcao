def verifica_ano(ano):
    if ano % 4 == 0:
        print(ano, "é um ano bissexto")
        
    else:
        print(ano, "não é um ano bissexto")
    
ano = int(input("Digite o ano para verificar se ele é bissexto ou não: "))

verifica_ano(ano)
