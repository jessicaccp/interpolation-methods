def gauss_seidel(n, A, b, eps, iter_max):
    # Vetor inicial de x
    x = [0,0,0]

    # Percorre todas as linhas da matriz
    for i in range(0,n):
        r = 1/A[i][i]

        # percorre todas colunas da matriz
        for j in range(0,n):
            if i != j:
                # Divide o valor dos elementos que não fazem parte da diagonal da 
                # matriz pelo o valor da diagonal correspondente aquela linha
                A[i][j] = A[i][j] * r
        
        # Divide o elemento do vetor resposta pelo valor da diagonal da matriz 
        # correspondente aquela linha
        b[i] = b[i] * r    

    # Quantidade de iterações
    k = 0

    while True:
      
        k = k + 1
        # Vetor que armazena os valores de x encontrados
        v = []

        # Percorre todas as linhas da matriz
        for i in range (0,n):
            soma = 0
            
            # Percorre todas as colunas da matriz
            for j in range(0,n):
                # Se não for um elemento da diagonal principal soma o valor 
                # do elemento multiplicado ao valor de x daquela linha a variavel soma
                if i != j:
                    soma = soma + A[i][j] * x[j]
            
            # Calcula o valor de x mais atualizado com relação aquela linha
            v[i] = b[i] - soma

        # Recebe o valor do critério de parada  
        d = teste_parada(n,x,v)

        # Verifica se d é menor ou igual que o eps ou se k maior que o número máximo de iterações
        if d <= eps or k >= iter_max:
            break
        
        # Atualiza o vetor x para os valores de x calculados na iteração
        x = v
    
    return x

# Calcula o critério de parada
def teste_parada(n, x, v): 

    # Valor do maior valor de x achado
    max_x = 0
    # Valor do maior valor achado entre a subtração do x da iteração atual com a passada
    max_norma = 0

    for i in range (0,n):
        # Verifica se o valor atual de x é o maior do vetor
        if max_x < v[i]:
            max_x = v[i]
        
        # Verifica se o valor atual da norma do valor antigo de x e do mais atualizado é o maior do vetor
        if max_norma < abs(v[i] - x[i]):
            max_norma = abs(v[i] - x[i])
    
    return abs(max_norma / max_x)