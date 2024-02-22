x = int(input())
z = int(input())
dh = ((x - 34) ** 2 + (z - 220) ** 2) ** (1/2)
dk = (x ** 2 + z ** 2) ** (1/2)
ds = ((x - 140) ** 2 + (z - 456) ** 2) ** (1/2)
print(f'Distancia para Hogsmeade: {dh:.2f}')
print(f'Distancia para Kakariko: {dk:.2f}')
print(f'Distancia para Solitude: {ds:.2f}')



