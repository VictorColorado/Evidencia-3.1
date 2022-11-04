while True:
    try:
        x = int(input("Introduce un múmero entero: "))
    except ValueError:
        print("No es dato válido. Intenta de nuevo...")
        
    else:
        print("Divide entre 50 /", x,"el resultado es :", 50/x)
    finally:
        print("Finalización de un programa.")