import random

DIFICULTAD_FACIL: int = 1
DIFICULTAD_DIFICIL: int = 2

dificultad: int
numeroSecreto: int
numeroIngresado: int
intentos: int

print("¿Qué dificultad quiere?")
while (True):
	print("1. Fácil")
	print("2. Difícil")
	
	dificultad = int(input())
	
	if (dificultad == DIFICULTAD_FACIL):
		numeroSecreto = random.randint(0, 20)
		intentos = 6
		break
	elif (dificultad == DIFICULTAD_DIFICIL):
		numeroSecreto = random.randint(0, 40)
		intentos = 5
		break
	
	print(dificultad, "no es una opción.")
	

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
