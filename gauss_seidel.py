def gauss_seidel(n, A, b, eps):

	# Verifica se a matriz converge
	teste_convergencia(n,A)

	# Número de iterações máximas
	iter_max = 10000
	# Vetor inicial de x 
	x = []
	# Vetor para os novos valores de x
	v = []
	
	# Inicializa com zero os vetores de x inicial e x atualizado do mesmo tamanho do vetor b
	for i in range(0,n):
		x.append(0)
		v.append(0)
	
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
		# Inicializa a váriavel que recebe o calculo do critério de parada
		d = 0
		# Incrementa o número de iterações
		k = k + 1

		# Percorre todas as linhas da matriz
		for i in range (0,n):
			# Inicializa a soma como 0
			soma = 0
			
			# Percorre todas as colunas da matriz
			for j in range(0,n):
				# Se não for um elemento da diagonal principal soma o valor 
				# do elemento multiplicado ao valor de x daquela linha a variavel soma
				if i != j:
					# Se for a primeira linha da matriz, x0
					if i == 0:
						soma = soma + A[i][j] * x[j]
					# Caso contrário, utiliza os valores de x já calculado		
					else: 
						soma = soma + A[i][j] * v[j]

			
			# Calcula o valor de x mais atualizado com relação aquela linha
			# e o valor de y da linha
			v[i] = b[i] - soma

		# Recebe o valor do critério de parada  
		d = teste_parada(n,x,v)
		
		# Atualiza o vetor x para os valores de x calculados na iteração
		for i in range(0, n):
			x[i] = v[i]

		# Verifica se d é menor ou igual que o eps 
		if d <= eps:
			return x
		# Verifica se k é maior que o número máximo de iterações
		elif k >= iter_max:
			break

# Calcula o critério de parada
def teste_parada(n, x, v): 

	# Valor do maior valor de x achado
	max_x = 0
	# Valor do maior valor achado entre a subtração do x da iteração atual com a passada
	max_norma = 0

	# Percorre o vetor
	for i in range (0,n):
		
		# Calcula o valor de x mais atualizado menos o anterior
		aux = abs(v[i] - x[i])

		# Verifica se a norma do valor atual de x é o maior armazenado 
		if max_x < abs(v[i]):
			max_x = abs(v[i])
		
		# Verifica se o valor atual da norma da subtração é a maior
		if max_norma < aux:
			max_norma = aux
	
	return abs(max_norma / max_x)

def teste_convergencia(n,A):

	beta = []
	soma = 0
	aux = 0
	
	# Inicializa o vetor beta
	for i in range(0,n):
		beta.append(0)

	# Percorre toda a matriz
	for i in range(0,n):
		for j in range(0,n):
			# Se não for um elemento da diagonal
			if i != j:
				# Se for a primeira linha da matriz
				if i == 0:
					# Soma os elementos da linha, exceto o valor da diagonal, dividido pelo valor da diagonal
					soma = soma + abs(A[i][j])/abs(A[i][i])
				# Caso contrario, soma os elementos da linha, exceto o valor da diagonal, multiplicado 
				# pelo valor de beta correspondente dividido pelo valor da diagonal
				else :
					soma = soma + abs(A[i][j])/abs(A[i][i]) * beta[i]
		
		# Adiciona o valor de beta encontrado	
		beta[i] = soma
		
		# Verifica se o valor encontrado é maior do que o anterior
		if aux < beta[i]:
			aux = beta[i]

	# Se o maior valor de beta for menor que um então o sistema irá convergir
	if aux < 1:
		print ("Converge")
	else:
		print("Não converge")
