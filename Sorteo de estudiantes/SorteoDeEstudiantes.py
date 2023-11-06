import random

estudiantes: list = [
	"Luis Menvoza",
	"Valeria Gías",
	"Martín Silba",
	"Isabella Montis",
	"Alejandro Ralcos",
	"Valentina Vargat",
	"Diego Gaxtillo",
	"Camila Rías"
]
listaAleatoria: list = []

for i in range(len(estudiantes)):
	index = random.randint(0, len(estudiantes) - 1)
	listaAleatoria.append(estudiantes.pop(index))

print(listaAleatoria)
print(estudiantes)