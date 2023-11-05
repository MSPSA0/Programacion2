import random



LETRAS = 'abcdefghijklmnñopqrstuvwxyzü';

IMAGENES_AHORCADO: list = [
'''
 +---+
 |   |
     |
     |
     |
     |
=========
''','''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''',
    '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
''','''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
''',
];

palabras: list = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo cebra'.split();



def obtenerPalabra(LISTA_DE_PALABRAS) -> str:
    return LISTA_DE_PALABRAS[random.randint(0, len(LISTA_DE_PALABRAS) - 1)];

def mostrarTablero(IMAGENES_AHORCADO, letrasCorrectas, letrasIncorrectas, palabraSecreta) -> None:
    palabraOculta: str = "";
    
    for letra in palabraSecreta:
        if (letra in letrasCorrectas):
            palabraOculta += letra;
        else:
            palabraOculta += '_ ';
    
    print("\n-------------------------------------------------------------------------------");
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)]);
    print("Palabra: " + palabraOculta);
    print("Letras incorrectas: " + letrasIncorrectas);
    print("\n");

def obtenerIntento(letrasProbadas) -> str:
    print("Ingrese una letra");
    letra: str = "";
    
    while (True):
        letra = input().strip().lower();
        
        if (letra in LETRAS):
            if (not letra in letrasProbadas):
                return letra;
            print("Esa letra ya se probó.");
        elif (len(letra) != 1):
            print("Tiene que ser una sola letra.");
        else:
            print("Tiene que ser una letra válida.");

def jugarDeNuevo() -> bool:
    print("¿Jugar de nuevo? (S/n)");
    respuesta: str = "";
    
    while (respuesta == ""):
        respuesta = input().strip().lower();
        
        if (respuesta == "s"):
            return True;
        elif (respuesta == "n"):
            return False;
        
        print(f"'{respuesta}' no es una opción válida.");
        respuesta = "";

def juego() -> None:
    palabra: str = obtenerPalabra(palabras);
    letrasCorrectas: str = "";
    letrasIncorrectas: str = "";
    
    while (len(letrasIncorrectas) < len(IMAGENES_AHORCADO) - 1):
        mostrarTablero(IMAGENES_AHORCADO, letrasCorrectas, letrasIncorrectas, palabra);
        letra = obtenerIntento(letrasCorrectas + letrasIncorrectas);
        
        if (letra in palabra):
            letrasCorrectas += letra;
            completado: bool = True;

            for letra in palabra:
                if (not letra in letrasCorrectas):
                    completado = False;
                    break;
            
            if (completado):
                break;
        else:
            letrasIncorrectas += letra;
    
    mostrarTablero(IMAGENES_AHORCADO, letrasCorrectas, letrasIncorrectas, palabra);
    print(f"""La palabra era: '{palabra.upper()}'

intentos: {len(letrasCorrectas) + len(letrasIncorrectas)}
intentos fallidos: {len(letrasIncorrectas)}
""");



juego();
while (jugarDeNuevo()):
    juego();
