import random
from statistics import mode, median, mean

# Crear una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Determinar el sesgo
if media > mediana > moda:
    sesgo = 'Sesgo positivo'
elif media < mediana < moda:
    sesgo = 'Sesgo negativo'
elif media == mediana == moda:
    sesgo = 'Sin sesgo'
else:
    sesgo = 'No se puede determinar el sesgo'

# Imprimir los resultados
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')
print(f'Media: {media}')
print(f'Sesgo: {sesgo}')
