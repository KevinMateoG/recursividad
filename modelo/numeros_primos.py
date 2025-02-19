
def es_primo(n, divisor=2):
    if n % divisor == 0:
        return False
    elif n % divisor != 0 and n % n == 0 and n % 1 ==0:
        return True
    return es_primo(n, divisor+1 )
print(es_primo())