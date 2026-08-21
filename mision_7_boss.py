energia_actual = int(input('cuanta energia tienes? '))
comida_encontrada = int(input('cuanta comida has encontrado? '))

def energia(energy, comida):
    energia_total = energy + comida
    return energia_total
def estado_slugcat(energia_total):
    if energia_total >= 10:
        print('Slugcat  (kuchu) esta bien, puedes seguir explorando')
    else: 
        print('Slugcat  (kuchu) esta mal, necesitas descansar y comer')

energia_total = energia(energia_actual, comida_encontrada)
estado_slugcat(energia_total)