def es_palindromo(cadena: str, idx: int = 0, cadena_dos: str =""):
    c = cadena.lower()
    if len(c) <= 1:
        return True
    if c == cadena_dos:
        return True
    if c[0] != c[-1]:
        return False
    return es_palindromo(cadena, idx-1, cadena_dos+c[idx-1])

print(es_palindromo("radar"))