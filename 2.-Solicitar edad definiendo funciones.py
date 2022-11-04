def solicitar_edad():
    try:
        return int(input("Escribe tu edad: "))
    except ValueError:
        return solicitar_edad()
edad = solicitar_edad()