# Solicitar el nombre del usuario
nombre = input('Por favor, ingresa tu nombre: ')

# Solicitar la opción deseada
opcion = int(input('Elige una opción (1, 2 o 3): '))

# Transformar el nombre según la opción seleccionada
if opcion == 1:
    resultado = nombre.upper()
elif opcion == 2:
    resultado = nombre.lower()
elif opcion == 3:
    resultado = nombre.title()
else:
    resultado = 'Opción no válida'

# Imprimir el resultado
print(resultado)
