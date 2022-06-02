def value():
    tempo = 6
    velocidade = 24
    distancia = calcular_distancia(tempo, velocidade)
    litros = litros(distancia)
    return distancia, litros
def resultado(values):
      distancia, litros = value()
      return f'O veículo percorreu ujma distancia de {distancia} km e utilizou {litros} litros de gasolina'