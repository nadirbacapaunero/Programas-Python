###Promedio de calificaciones

''' Este agloritmo lee calificaciones de alumnos y
calcula el promedio de semestre '''

'''
Nombre    1   2   3   4   5    6

Pedro     8   9  7.8 8.1  7.2  9.5
Maria     8.6 10  10 9.4  9.7  9.3
Alejandro 9.5 6.4 8.9 8.9 9.9 10

'''

no_est = int(input('Dame el numero de alumnos: \n'))

no_califs = int(input('Dame el numero de calificaciones por alumno: \n'))

for cont_est in range (no_est):
    print('Dame el nombre del estudiante ?')
    nombre_est = input()
    contador_calificaciones = 1
    suma = 0.0

    while (contador_calificaciones <= 6):
        print( 'Dame una calificacion :')
        calificacion = float(input())
        suma = suma + calificacion
        contador_calificaciones += 1

    promedio = suma/6.0
    print('Promedio del estudiante ', nombre_est , 'es:',  promedio)


