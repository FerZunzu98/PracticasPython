def cambiar_base_num(n, base):

    if not n: return 0

    potencia = 0

    while n > base**potencia:
        potencia +=1
    print("potencia",potencia)
    respuesta = {}

    while n:
        if base ** potencia <= n:
    
            respuesta[potencia] = n // (base**potencia)
            n = n % (base** potencia)
    
        potencia -=1

    print(respuesta)

    resultado = ""
    for i in range(max(respuesta.keys()),-1,-1):            
    
        resultado += str(respuesta[i]) if i in respuesta.keys() else "0"
        
    print(int(resultado))
    return resultado


cambiar_base_num(4545,7)