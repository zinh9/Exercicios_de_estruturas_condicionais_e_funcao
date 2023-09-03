def verifica_idade(idade):
    if idade >= 18:
        print("Você é de maior e pode votar")
    
    else:
        print("Você é de menor e não ṕode votar")

idade = int(input("Digite a sua idade para saber se você pode votar ou não: "))

verifica_idade(idade)
