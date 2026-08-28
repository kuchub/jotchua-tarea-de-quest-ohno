class slugcat:
    def __init__(self, nombre, region, energia):
        self.nombre = nombre
        self.region = region
        self.energia = energia
    def comida(self, puntos_comida):
        self.energia = self.energia + puntos_comida 
        print(f'tu personaje ha comido y ahora tiene {self.energia} de comida')
    def moverse(self, moverse):
        self.energia= self.energia - moverse
        print(f'slugcat se ha movido y ahora   tiene {self.energia} de energia')

silly = slugcat('kuchu', 'outside', 5)
silly.comida(1)
silly.moverse(2)