import numpy;
import matplotlib;
import random;
import matplotlib.pyplot as pyplot;

pyplot.rcParams["image.cmap"] = "gray";

ancho: int = 300;
alto: int = 300;

matriz = numpy.array([[0] * ancho] * alto);

for y in range(alto):
    for x in range(ancho):
        matriz[y][x] = random.randint(0, 255);

pyplot.imshow(matriz);
pyplot.show();

