# datos del slug
slugcat = {
    'nombre': 'Kuchu',
    'región': 'Outskirts',
    'refugio': True
}
inventory = ['bloque', 'lanza']

# datos del slugcat
print(f'Slugcat: {slugcat["nombre"]} | Region: {slugcat["región"]}')
inventory.append(input('que mas encontraste¿ '))

for item in inventory:
    print('en tu invetario tienes:', item)