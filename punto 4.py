import random

# Generar una lista aleatoria de máximo 10 números entre negativos y positivos
longitud = random.randint(1, 10)
numeros = [random.randint(-100, 100) for _ in range(longitud)]

# Función que imprime cuáles números son positivos
def imprimir_numeros_positivos(lista):
    positivos = [num for num in lista if num > 0]
    if positivos:
        print("Los números positivos son:", positivos)
    else:
        print("No hay números positivos en la lista.")

# Imprimir la lista generada y llamar a la función
print("Lista generada:", numeros)
imprimir_numeros_positivos(numeros)
print("la cantidad de numeros positivoss es:", len(numeros))