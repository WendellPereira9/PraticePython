

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

matriz

matriz.shape

soma = 0
for i in range(matriz.shape[0]):
  print(matriz[i])
  for j in range(matriz.shape[1]):
    soma += matriz[i][j]
    print('Soma: ', soma)