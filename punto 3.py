## Ejercicio #3
# funcion
def obtener_primero_ultimo(lista):
    # Verificar que la lista no este vacia
    if lista:
        # Verificar que la lista tenga 2 o mas elementos
        if(len(lista)>=2):
            return (lista[0], lista[-1])
        else:
            return "la lista no tiene elementos suficientes"
    else:
        return "dato no valido. lista vacia"

# Invocar funcion
lista_1 = []
resultado = obtener_primero_ultimo(lista_1)
print(resultado)