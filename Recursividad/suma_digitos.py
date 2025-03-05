def suamr_digitos(num: int, sum = 0):
    if num == 0:
        return sum
    sum = sum + (num%10)
    num = num // 10
    return suamr_digitos(num, sum)

print(suamr_digitos(81))