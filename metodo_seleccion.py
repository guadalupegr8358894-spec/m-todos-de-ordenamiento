def por_seleccion(arr):
    n = len(arr)
    for i in range(n):
        # Suponer que el primer elemento no ordenado es el mínimo
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiar el elemento mínimo encontrado con el primero
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# --- Ejercicio de prueba ---
if __name__ == "__main__":
    datos_seleccion = [29, 10, 14, 37, 14, 33, 8, 11]
    print("\n--- Método por Selección ---")
    print("Lista original:", datos_seleccion)
    resultado = por_seleccion(datos_seleccion)
    print("Lista ordenada:", resultado)