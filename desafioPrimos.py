# Código para solução do desafio do curso AWS re/Start
# 141-[PF]-Lab - [Challenge] Python Exercise
#
# # Autor:      Mário A L Velloso
# Data:         14 nov 2021
# Objetivo:     Escrever todos os números primos entre 1 e 250 e armazenar estes resultados em um
#               arquivo de nome results.txt

def ePrimo(numero):
    # Se for menor que 2, não pode
    if numero < 2:
        return False
    
    # O 2 é o único número primo par
    elif numero == 2:
        return True
    
    # Se for 3 ou maior, vamos testar se é primo
    else:
        # Zero o contador de divisores
        divisores = 0

        # Percorro todos os número menores que o número passado até a metade do número (nao faz sentido testar após a metade)
        for i in range(2, (numero + 2) // 2):
            if numero % i == 0:
                divisores += 1
                # Se houver algum divisor, não é primo e paro o loop para economizar tempo
                break
        
        if divisores > 0:
            # Se houver divisores para o número, então ele não é primo
            return False
        else:
            return True

# Vamos abrir o arquivo texto para salvar os resultados
f = open("results.txt", "w")    

# Vamos percorrer os números de 1 a 250
for j in range (1, 251):
    if ePrimo(j):
        print(f'O número {j} é primo!')
        f.write(str(j) + ';')
    else:
        print(f'O número {j} NÃO é primo!')

# Vamos fechar o arquivo texto
f.close()

            
