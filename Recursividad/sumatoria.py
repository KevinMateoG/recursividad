def sumatoria(lista: list[int], idx:int=0, sumar:int=0) -> int:
    if idx >= len(lista) :
        return sumar
    return sumatoria(lista, idx+1, sumar+lista[idx])

print(sumatoria([1, 2, 3, 4, 5]))  #! Output: 15
print(sumatoria([10, -5, 7]))      #! Output: 12
print(sumatoria([10, -2, 8, -3, 7])) #! 20
print(sumatoria([0, 5, 10, 0, -5])) #! 10
print(sumatoria([1000000, 2000000, 3000000, -1000000])) #! 5000000
"hola"