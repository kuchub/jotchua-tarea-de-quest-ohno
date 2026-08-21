# hacer un elif con la lluvia 
time_rain = int(input('cuanto tiempo tienes antes que caiga la lluvia¿'))

if time_rain >= 10:
    print('biem, aun tienes tiempo..')
elif time_rain >= 5:
    print('te falta poco tiempo.. apresurate')
else:
    print('la lluvia se avecina.')