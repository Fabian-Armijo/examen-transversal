import random
import csv
import statistics
import time

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']



def sueldos():
    trabajador_sueldo = []
    for fila in trabajadores:
        sueldo_random = random.randint(300000,2500000)
        trabajador = [fila,sueldo_random]
        trabajador_sueldo.append(trabajador)
    return trabajador_sueldo

def clasificar_sueldos(matriz):
    menores = []
    intermedio = []
    mayores = []
    for fila in matriz:
        if fila[1] < 800000:
            menores.append(fila)
        if fila[1] >= 800000 and fila[1] < 2000000:
            intermedio.append(fila)
        if fila[1] > 2000000:
            mayores.append(fila)
    print(f'Sueldos menores a $800.000 TOTAL: {len(menores)}')
    print('Nombre empleado\tSueldo')
    for fila in menores:
        print(f'{fila[0]}\t{fila[1]}')
    print()
    print(f'Sueldos entre $800.000 y $2.000.000 TOTAL: {len(intermedio)}')
    print('Nombre empleado\tSueldo')
    for fila in intermedio:
        print(f'{fila[0]}\t{fila[1]}')
    print()
    print(f'Sueldos mayores a $2.000.000 TOTAL: {len(mayores)}')
    print('Nombre empleado\tSueldo')
    for fila in mayores:
        print(f'{fila[0]}\t{fila[1]}')
    
    sueldo_total = 0
    for fila in matriz:
        sueldo_total += fila[1]
    print(f'TOTAL SUELDO: ${sueldo_total}')
    
    
def ver_estadisticas(matriz):
    max_sueldo = 0
    sueldos = 0
    promedio_sueldos = 0
    for fila in matriz:
        if fila[1] > max_sueldo:
            max_sueldo = fila[1]
    
    for fila in matriz:
        min_sueldo = fila[1]
        if fila[1] < min_sueldo:
            min_sueldo = fila[1]
    contador = 0
    for fila in matriz:
        if fila[1]:
            contador +=1
            sueldos += fila[1]
    
    promedio_sueldos = round(sueldos / contador,1)
    media_sueldos = []
    for fila in matriz:
        media_sueldos.append(fila[1])
    
    media_geometrica = round(statistics.geometric_mean(media_sueldos),1)
        
    print('*'*20)
    print(f'Sueldo mas alto: {max_sueldo}')
    print(f'Sueldo mas bajo: {min_sueldo}')
    print(f'Promedio de sueldos: {promedio_sueldos}')
    print(f'Media geometrica: {media_geometrica}')
    print('*'*20)
    
def reporte_sueldos(matriz):
    with open('reporte_de_sueldos.csv','w',newline='') as archivo_csv:
        escribir = csv.writer(archivo_csv)
        escribir.writerow(['Nombre empleado' , 'Sueldo base' , 'Desc. salud' , 'Desc AFP' , 'Sueldo liquido'])
        for fila in matriz:
            desc_salud = int(fila[1] * 0.07)
            desc_afp = int(fila[1] * 0.12)
            sueldo_liquido = int(fila[1] - (desc_afp + desc_salud))
            trabajador = [fila[0],fila[1],desc_salud,desc_afp,sueldo_liquido]
            escribir.writerow(trabajador)


sueldos_trab = sueldos()
while True:
    print('-'*20)
    print('1.-Asignar sueldos aleatorios')
    print('2.-Clasificar sueldos')
    print('3.-Ver estadisticas')
    print('4.-Reporte de sueldos')
    print('5.-Salir del programa')
    print('-'*20)
    opc = int(input('Ingrese su opcion: '))
    match opc:
        case 1:
            print(sueldos())
        case 2:
            clasificar_sueldos(sueldos_trab)
        case 3:
            ver_estadisticas(sueldos_trab)
        case 4:
            reporte_sueldos(sueldos_trab)
        case 5:
            print('Finalizando programa...')
            time.sleep(1)
            print('Desarrollado por Fabian Armijo')
            print('18.777.555-8')
            break
        case _:
            pass