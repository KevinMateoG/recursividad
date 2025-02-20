def es_primo(n, divisor=2):
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return es_primo(n, divisor+1 )

print(es_primo(17))