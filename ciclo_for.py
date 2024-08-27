print('Comienzo')

""" for i in [1, 2, 3]:
    print(f'Hola, ahora i vale {i} y su cuadrado es {i ** 2}') """
numero = int(input('numero que queire la tabla de multipiclar '))

print(f'Tabla de multiplicar del numero {numero}')

for i in range(1, 11):
    print(f'{i} x {numero} = {i * numero}')
    
print('Final')