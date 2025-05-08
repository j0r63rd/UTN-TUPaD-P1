# Solicitar información al usuario
hemisferio = input('¿En qué hemisferio te encuentras? (N/S): ').upper()
mes = int(input('¿Qué mes del año es? (1-12): '))
dia = int(input('¿Qué día es? (1-31): '))

# Determinar la estación según el hemisferio y la fecha
if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):
        estacion = 'Invierno'
    elif (mes == 3 and dia >= 21) or (mes <= 5) or (mes == 6 and dia <= 20):
        estacion = 'Primavera'
    elif (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia <= 20):
        estacion = 'Verano'
    elif (mes == 9 and dia >= 21) or (mes <= 11) or (mes == 12 and dia <= 20):
        estacion = 'Otoño'
else:
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):
        estacion = 'Verano'
    elif (mes == 3 and dia >= 21) or (mes <= 5) or (mes == 6 and dia <= 20):
        estacion = 'Otoño'
    elif (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia <= 20):
        estacion = 'Invierno'
    elif (mes == 9 and dia >= 21) or (mes <= 11) or (mes == 12 and dia <= 20):
        estacion = 'Primavera'

# Imprimir la estación
print(f'La estación es: {estacion}')
