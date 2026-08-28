class slugcat:
    def __init__(self, nombre, region, energia):
        self.nombre = nombre
        self.region = region
        self.energia = energia

    def moverse(self, moverse):
        self.energia = self.energia - moverse

    def vivo(self):
        if self.energia > 0:
            print('slugcat sigue vivo')
        else:
            print('slugcat ha muerto')

bobis = slugcat('kuchu', 'afuera', 2)
bobis.moverse(1)
bobis.vivo()