def contar_digitos(num: int, contador:int=0) -> int:
    if num < 0:
        num = num*-1
    if num >= 0:
        if num < 10:
            return contador+1
    return contar_digitos(num//10, contador+1)

print(contar_digitos(12345)) # Output: 5
print(contar_digitos(987654))  # Output: 6
print(contar_digitos(1231244))
print(contar_digitos(-12333))