comida = 0
ciclos = 1

while comida < 4:
    decision = input('buscaras comida o descansaras? ')

    if decision == 'comida':
        print('bien!, has encotrado comida')
        comida = comida + 1
    elif decision == 'descansar':
        print('no has encontrado nada,,, pero has descansado')
        ciclos = ciclos + 1
    else:
        print('accion invalida,, vuelvelo a intentar!')

print(f'bien, lo lograste!, en total han pasado {ciclos} ciclos ')

'''
while comida < 4:
    decision = input('buscaras comida o descansaras? ')

    if decision == 'comida':
        print('bien!, has encotrado comida')
        comida = comida + 1
    else:
        print('no has ido a buscar... pero has descansado')
        ciclos = ciclos + 1
'''