# comida recolectada
food_txt = input('cuanta comida has recolectado¿')
food_num = int(food_txt)
#ciclos
ciclos_txt = input('cuantos ciclos han pasado¿ ')
ciclos_num = int(ciclos_txt)

food_rest = food_num - (ciclos_num * 2)

#contenido
content = f'''el slugcat en su dia ha recoletado {food_num} bayas, y se fue a su refugio,
asi mismo hibernando, quedanto en total su barra de comida en: {food_rest}'''

print(content)