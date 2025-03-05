def es_primo(n, divisor=2):
    if n == 2:
        return True
    if n == divisor:
        return True
    if n % divisor == 0:
        return False
    return es_primo(n, divisor+1 )

print(es_primo(60))