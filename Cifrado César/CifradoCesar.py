"""
El usuario debe ingresar una palara y un
desplazamiento (+ o -) y aplicar Cifrado César.
"""
ABECEDARIO: str = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

palabra: str
palabraCifrada: str
desplazamiento: int

def cifrarAbecedario(texto: str, desplazamiento: int) -> str:
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

def cifrarASCII(texto: str, desplazamiento: int) -> str:
    textoCifrado: str = ""
    for c in texto:
        textoCifrado += chr(ord(c) + desplazamiento)
    return textoCifrado

def cifrar(texto: str, desplazamiento: int) -> str:
    textoCifrado: str = ""
    for c in texto:
        if (c.islower()):
            limite = ord('z') - ord('a') + 1
            letraA = ord('a')
        else:
            limite = ord('Z') - ord('A') + 1
            letraA = ord('A')
        textoCifrado += chr(letraA + ((ord(c) - letraA + desplazamiento) % limite))
    return textoCifrado

print("Ingrese la palabra")
palabra = input()

print("Ingrese el desplazamiento")
desplazamiento = int(input())

palabraCifrada = cifrar(palabra, desplazamiento)

print(palabraCifrada)
