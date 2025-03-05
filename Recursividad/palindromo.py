def es_palindromo(cadena: str, idx: int = 0, idx_2 = 0,cadena_dos: str =""):
    c = cadena.lower()
    if len(c) <= 1:
        return True
    
    if c == cadena_dos:
        return True
    
    if idx == len(c):
        return False
    return es_palindromo(cadena, idx+1, idx_2-1, cadena_dos+c[idx_2-1])

print(es_palindromo("radat"))