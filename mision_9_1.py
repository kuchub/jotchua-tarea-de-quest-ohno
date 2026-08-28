class slugcat:
    def __init__(self, nombre, region, karma):
        self.nombre = nombre
        self.region = region
        self.karma = karma

sillyslug = slugcat('kuchu', 'outside', 5) 

print(f'mi slug cat se llama {sillyslug.nombre} se encuentra en la region {sillyslug.region}')
print(f'y tiene {sillyslug.karma} puntos de karma')