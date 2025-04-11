
with open("informacion.txt", "r", encoding="utf-8") as archivo:
   
    lineas = archivo.readlines()[1:]

    for i, linea in enumerate(lineas, start=1):
        linea = linea.strip()
        partes = linea.split(";")

        if len(partes) != 4:
            print(f"[Línea {i}] Error de formato: {linea}")
            continue

        nombre = partes[0]
        apellido = partes[1]
        direccion = partes[2]
        correo = partes[3]
        
        print(f"Registro {i}")
        print(f"  Nombres:   {nombre}")
        print(f"  Apellidos: {apellido}")
        print(f"  Dirección: {direccion}")
        print(f"  Correo:    {correo}")
        print("-" * 50)
