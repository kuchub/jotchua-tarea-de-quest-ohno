class slugcat:
    def __init__(self, nombre, salud, fuerza): 
        self.nombre = nombre
        self.salud = salud
        self.fuerza = fuerza
    def vivo(self):
        if self.salud > 0:
            return True
        else:
            return False
    def daño_recibido(self, cantidad):
        self.salud = self.salud - cantidad
    def atacar(self, objetivo):
        objetivo.daño_recibido(self.fuerza)

# datos del slug
kuchu = slugcat('kuchu', 6, 10)
lagarto = slugcat('caramel', 10, 15)

class lagarto:
    def __init__(self, nombre, salud, fuerza):
        self.nombre = nombre
        self.salud = salud
        self.fuerza = fuerza

while True:
    print('\n - - - prueba - - -')
    print('1. ver datos..')
    print('2. atacar')
    print('3. salir')
    print('4. guardar partida')
    print('5. cargar partida')

    opcion = input('eligue una opcion! ')
    if opcion == '1':
        print('mostrar datos..')
        print(f'nombre: {kuchu.nombre} | salud: {kuchu.salud} | fuerza: {kuchu.fuerza}')
    elif opcion == '2':
        kuchu.atacar(lagarto)
        print(f'{kuchu.nombre} ha atacado a {lagarto.nombre}, este le queda {lagarto.salud} puntos de vida')
    elif opcion == '3':
        print(f'okei, adios')
        break
    elif opcion == '4':
        with open('partida_final.txt', 'w') as archivo:
            archivo.write(f'slugcat: {kuchu.nombre} | salud: {kuchu.salud} | fuerza: {kuchu.fuerza}')
    elif opcion == '5':
        try:
            with open('partida_final.txt', 'r') as archivo:
                datos = archivo.read()
            print(f'datos guardados \n{datos}')
        except FileNotFoundError:
            print('no hay ninguna partida guardada')
    else:
        print('opcion no valida, intenta denuevo')

