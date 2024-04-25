def collatz_function(x, string):
    if string.upper() == 'C': # Elegimos qué función iterar en función de la entrada
        # par
        if x % 2 == 0:
            return x // 2  # División entera
        # impar
        else:
            return 3 * x + 1
    else:
        # par
        if x % 2 == 0:
            return x // 2  # División entera
        # impar
        else:
            return (3 * x + 1) // 2
        

