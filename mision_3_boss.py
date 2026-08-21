food = int(input('cuanta comida tienes¿ '))
food_ate = int(input('cuanta comida has comido hoy¿'))
weapons = int(input('cuantas lanzas tienes¿ '))
kills = input('que creaturas has matado? ')
ciclos_past = int(input('cuantos ciclos han pasado¿ '))
food_total = food + food_ate

# comida despues de ciclo
food_aftercicle = food_total - (ciclos_past * 2)


# texto sobre la comida, kills y weapons
texto = f'''
el slugcat ha recolectado {food} bayas, tiene {weapons} lanzas y ha matado a {kills}
y despues de {ciclos_past}, el slugcat tiene {food_aftercicle} de comida
'''
# print
print(texto)
