x = [12,3,4,5,6,90]
def contar_elementos(lista: list[int], idx = 0) -> int:
    if idx == len(lista):
        return idx
    return contar_elementos(lista, idx +1)

def encontrar_elemento(lista: list[int], num: int, idx=0):
    if idx >= len(lista):
        return False
    if num == lista[idx]:
        return True
    return encontrar_elemento(lista, num, idx+1)


print("--------contar elmentos--------")
print(contar_elementos(x))

print("--------encontrar_elementos--------")
print(encontrar_elemento(x, 90))