import numpy;
import matplotlib;
import matplotlib.pyplot as pyplot;

pyplot.rcParams["image.cmap"] = "gray";

ancho: int = 300;
alto: int = 300;

matriz = numpy.array([[0] * ancho] * alto);

pyplot.imshow(matriz);
pyplot.show();
