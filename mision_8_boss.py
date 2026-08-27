nombre = (input('como te llamas¿'))
ciclos = int(input('cuantos ciclos han pasado¿'))

def guardar_partida(nombre, ciclos):
    with open('partida.txt', 'w') as content:
        content.write(f'tu nombre es {nombre} y han pasado {ciclos} ciclos')
        return content.write

def cargar_partida():
    try:
        with open('partida.txt', 'r') as partida:
            partida.read()
    except FileNotFoundError:
        print('archivo no encontrado')
        return partida.read