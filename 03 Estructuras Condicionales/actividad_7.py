# Solicitar una frase o palabra al usuario
frase = input('Por favor, ingresa una frase o palabra: ')

# Verificar si el último carácter es una vocal
if frase[-1].lower() in 'aeiou':
    frase += '!'

# Imprimir el resultado
print(frase)
