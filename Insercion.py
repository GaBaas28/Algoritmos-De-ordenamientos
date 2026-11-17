def ordenamiento_insercion(temperaturas):
    # Comenzar desde el segundo elemento
    for i in range(1, len(temperaturas)):
        clave = temperaturas[i]
        j = i - 1
        
        # Mover los elementos mayores que la clave una posición hacia adelante
        while j >= 0 and clave < temperaturas[j]:
            temperaturas[j + 1] = temperaturas[j]
            j -= 1
        
        # Insertar la clave en su posición correcta
        temperaturas[j + 1] = clave
    return temperaturas

# Prueba del algoritmo
temps = [22.5, 18.0, 25.4, 20.1, 19.8]
print("Temperaturas desordenadas:", temps)
print("Temperaturas ordenadas:", ordenamiento_insercion(temps))