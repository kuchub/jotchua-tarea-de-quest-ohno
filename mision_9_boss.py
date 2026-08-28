class slugcat:
    def __init__(self, nombre, salud, fuerza,):
        self.nombre = nombre
        self.salud = salud
        self.fuerza = fuerza

    def atacar(self, objetivo):
        objetivo.salud = objetivo.salud - self.fuerza
        print(f'te quedan {objetivo.salud} de vida')

    def vivo(self):
            if self.salud > 0:
                print(f'esta vivo')
            else:
                print(f'ha muerto')

kuchu = slugcat('kuchu', 7, 5)
lagarto = slugcat('color', 6, 6)

kuchu.atacar(lagarto)
lagarto.vivo()