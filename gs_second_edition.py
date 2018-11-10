def gauss_seidel_se(dimension, A, b, error):
  x = [0] * dimension
  aux = {}
  iterations = 20
  y = [0] * dimension

  for i in range(0, dimension):
    aux[i] = []
    
  while iterations:
    for i in range(0, dimension):
      y[i] = (b[i] / A[i][i]) 
      for j in range(0, dimension):
        if i == j: continue
        y[i] -= (A[i][j] / A[i][i] * x[j])
        x[i] = y[i]
      aux[i].append(y[i])
    if stop_test(aux, 0.5): 
      return y
    iterations -= 1
  return y

def stop_test(aux, error):
  flag = [False] * 3
  for i in range(0, len(aux)):
    max_difference = -1
    max_value = -1
    aux[i].sort();
    for j in range(i + 1, len(aux[i]) - 1):
      if abs(aux[i][j] - aux[i][j - 1]) > max_difference:
        max_difference = abs(aux[i][j] - aux[i][j - 1])
        max_value = abs(aux[i][j])
    if max_difference / max_value <= error:
      flag[i] = True
  for f in flag:
    if f == False: return False
  return True  
