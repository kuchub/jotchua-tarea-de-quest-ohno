def curar_slugcat(salud_actual, curacion):
    hp_new = salud_actual + curacion
    return hp_new

vida_slug = 4
vida_slug = curar_slugcat(vida_slug, 5)
print(f'el slug cat ha comido y se ha curado, ahora tiene {vida_slug} de vida')