def ler_temperatura():
    temperatura1 = float(input('Digite numero graus celsius: '))
    return temperatura1

def converster(temperatura_celsius):
    temperatura_f = (9 * temperatura_celsius + 16) / 5
    return temperatura_f