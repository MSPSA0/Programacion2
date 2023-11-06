import random


numeroSecreto: int = random.randint(0, 20)
numeroIngresado: int
intentos: int = 6

while (True):
	print(f"Ingrese el número ({intentos} intento{'s' if intentos > 1 else ''})")
	numeroIngresado = int(input())
	
	if (numeroIngresado == numeroSecreto):
		print("El número era", numeroIngresado)
		break
	elif (numeroIngresado > numeroSecreto):
		print("El número es más chico")
	else:
		print("El número es más grande")
	
	intentos -= 1
	if (intentos <= 0):
		print("Ya no hay más intentos")
		print("En número era", numeroSecreto)
		break
