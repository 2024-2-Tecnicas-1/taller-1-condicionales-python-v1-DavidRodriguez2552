def evaluar(caracter):
 codigo_ascii = ord(caracter)
 if '0' <= caracter <= '9':
    return "Es número"
 elif 'A' <= caracter <= 'Z':
    return "Es letra mayúscula"
 elif 'a' <= caracter <= 'z':
    return "Es letra minúscula"
 else:
    return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
