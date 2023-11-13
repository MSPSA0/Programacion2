"""
El usuario debe ingresar una palara y un
desplazamiento (+ o -) y aplicar Cifrado César.
"""
ABECEDARIO: str = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

palabra: str
palabraCifrada: str
desplazamiento: int

print("Ingrese la palabra")
palabra = input()

print("Ingrese el desplazamiento")
desplazamiento = int(input())

palabraCifrada = ""
for c in palabra:
    indice = ABECEDARIO.find(c.upper())
    if (indice >= 0):
        esMinuscula = c.islower()
        c = ABECEDARIO[indice + desplazamiento]
        if (esMinuscula):
            c = c.lower()
    palabraCifrada += c

print(palabraCifrada)
