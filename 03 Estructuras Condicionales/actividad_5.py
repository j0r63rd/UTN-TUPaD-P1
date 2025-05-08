# Solicitar la contraseña del usuario
contrasena = input('Por favor, ingresa una contraseña (8 a 14 caracteres): ')

# Verificar la longitud de la contraseña
if 8 <= len(contrasena) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')
