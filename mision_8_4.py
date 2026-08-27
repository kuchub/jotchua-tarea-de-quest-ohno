try:
    contenido = int(input('cuanto karma tienes (1 a 6)'))
    print(f'bien.. tienes un nivel de karma de {contenido}')
except ValueError:
    print('debes ingresar un numero.')