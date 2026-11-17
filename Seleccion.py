def ordenamiento_seleccion(precios):
    n = len(precios)
    for i in range(n):
        # Encontrar el índice del elemento mínimo en el resto de la lista
        indice_minimo = i
        for j in range(i + 1, n):
            if precios[j] < precios[indice_minimo]:
                indice_minimo = j
                
        # Intercambiar el elemento mínimo encontrado con el primer elemento desordenado
        precios[i], precios[indice_minimo] = precios[indice_minimo], precios[i]
    return precios

# Prueba del algoritmo
costos = [150.50, 45.00, 299.99, 10.00, 85.50]
print("Precios desordenados:", costos)
print("Precios ordenados:", ordenamiento_seleccion(costos))