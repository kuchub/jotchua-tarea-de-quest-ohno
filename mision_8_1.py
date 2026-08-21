slugcat = 'kuchu'
zona = 'outskirts'
with open('registro.txt', 'w') as partida:
    partida.write(f'el nombre del slugcat es {slugcat}\n')
    partida.write(f'la zona en la que estas es {zona}')

print('guardado completado')