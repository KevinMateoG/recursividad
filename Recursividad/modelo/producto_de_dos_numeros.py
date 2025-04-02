def producto(a:int, b:int, cont:int=0, suma:int=0):
    if a == cont >=1:
        return suma
    return producto(a, b, cont+1, suma+b)

print(producto(3, 4))# Output: 12)
print(producto(5, 6))# Output: 30)
print(producto(5, 1))# Resultado esperado: 5
print(producto(7, 0))  # Resultado esperado: 0
print(producto(0, 8))  # Resultado esperado: 0
print(producto(3, 4))  # Resultado esperado: 12
print(producto(6, 2))  # Resultado esperado: 12
