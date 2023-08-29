# Problema 1  / 8 ptos x4 pruebas / 32 puntos
# Concatenación de listas o tuplas
# --------------------------------
# Confeccione un programa que lea 2 tuplas sean t1 y t2
# La salida debe ser una tupla en el orden t2 t1 t2
# ---------------------------------
# Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
# La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
def cambioInt(lista):
    for i in range(len(lista)):
        try:
            lista[i] = int(lista[i])
        except ValueError:
            continue


t = input().split()
m = input().split()
cambioInt(t)
cambioInt(m)
tupla1 = tuple(t)
tupla2 = tuple(m)
print(tupla2 + tupla1 + tupla2)
