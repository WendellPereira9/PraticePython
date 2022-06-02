tempo = input('Qual foi o tempo gasto na viagem?:') # em horas
velocidade = input('Qual a velocidade média do veículo durante a viagem?:') # em km/hora
distancia = int(tempo) * int(velocidade)
litros_usados = distancia / 12
print(f'O tempo gasto na viagem foi de {tempo} horas, numa velocidade de {velocidade} km/horas. A distância percorrida foi de {distancia} km e {litros_usados} litros de gasolina foram utilizados') 
