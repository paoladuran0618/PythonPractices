# -*- coding: utf-8 -*-

calificaciones = {}
calificaciones['algoritmos'] = 19
calificaciones['matematicas'] = 20
calificaciones['web'] = 18
calificaciones['bases_de_datos'] = 20

for key in calificaciones:
    print(key)

for value in calificaciones.values():
    print(value)

for key, value in calificaciones.items():
    print('Llave: {}, valor: {}'.format(key, value))

sum_calificaciones = 0
for calificacion in calificaciones.values():
    sum_calificaciones += calificacion

promedio = sum_calificaciones / len(calificaciones.values())
print('Nuestro promedio es: {}'.format(promedio))