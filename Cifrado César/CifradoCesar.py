"""
El usuario debe ingresar una palara y un
desplazamiento (+ o -) y aplicar Cifrado César.
"""
ABECEDARIO: str = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

palabra: str
palabraCifrada: str
desplazamiento: int

def cifrar(texto: str, desplazamiento: int) -> str:
    textoCifrado: str = ""
    for c in texto:
        indice = ABECEDARIO.find(c.upper())
        if (indice >= 0):
            esMinuscula = c.islower()
            c = ABECEDARIO[indice + desplazamiento]
            if (esMinuscula):
                c = c.lower()
        textoCifrado += c
    return textoCifrado

print("Ingrese la palabra")
palabra = input()

print("Ingrese el desplazamiento")
desplazamiento = int(input())

palabraCifrada = cifrar(palabra, desplazamiento)

print(palabraCifrada)
