def maior(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        print(num_1, "é o maior")
    
    elif num_2 > num_1 and num_2 > num_3:
        print(num_2, "é maior")
    
    elif num_3 > num_1 and num_3 > num_2:
        print(num_3, "é maior")

num_1 = float(input("Digite o primeiro numero: "))
num_2 = float(input("Digite o segundo numero: "))
num_3 = float(input("Digite o terceiro numero: "))

maior(num_1, num_2, num_3)
