def ordenamiento_burbuja(calificaciones):
    n = len(calificaciones)
    # Recorrer todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento actual es mayor que el siguiente
            if calificaciones[j] > calificaciones[j + 1]:
                calificaciones[j], calificaciones[j + 1] = calificaciones[j + 1], calificaciones[j]
    return calificaciones

# Prueba del algoritmo
grados = [85, 92, 78, 60, 89, 73]
print("Calificaciones desordenadas:", grados)
print("Calificaciones ordenadas:", ordenamiento_burbuja(grados))