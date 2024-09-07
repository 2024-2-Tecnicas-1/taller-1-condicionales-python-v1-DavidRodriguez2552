def evaluar(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    if residuo == 0:
        respuesta = "La división es exacta. \nCociente: {}\nResiduo: {}".format(cociente, residuo)
    else:
        respuesta = "La división no es exacta. \nCociente: {}\nResiduo: {}".format(cociente, residuo)

    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)