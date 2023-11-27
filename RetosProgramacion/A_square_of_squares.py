def is_square(n): 
    
    if n < 0: return False
    
    return True if str(n**(1/2)).split(".")[1] == "0" else False

def is_square_s2(n):    
    return n >= 0 and (n**0.5) % 1 == 0


is_square(2)