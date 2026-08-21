def energia(comida, comida_hibernar):
    if comida >= comida_hibernar:
        return True
    else:
        return False

entrar = energia(6, 5)
if entrar:
    print('puedes hibernar tranquilamente')
else:
    print('no puedes hibernar, necesitas mas comida')