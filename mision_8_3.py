try:
    with open('archivo_fantasma.txt', 'r') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print('partida no encontrada')