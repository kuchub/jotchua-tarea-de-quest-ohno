food = int(input('cuanto de comida tienes¿ '))
enemies = int(input('cuantos enemigos hay¿'))
rain = input('esta lloviendo¿ (si/no)')

if food >= 4 and rain == 'si'   :
    print('puedes hibernar..')
elif enemies >= 1 or rain == 'si':
    print('ten cuidado.')
else:
    print('mantente resguardado')