def insercion(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        # Mover los elementos de la lista que son mayores que la clave
        # a una posición adelante de su posición actual
        while j >= 0 and key_check(arr[j], clave): # o simplemente arr[j] > clave
            pass # (usando la lógica estándar abajo)
            
def por_insercion(arr):
    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > actual:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = actual
    return arr

# --- Ejercicio de prueba ---
if __name__ == "__main__":
    datos_insercion = [12, 11, 13, 5, 6]
    print("\n--- Método por Inserción ---")
    print("Lista original:", datos_insercion)
    resultado = por_insercion(datos_insercion)
    print("Lista ordenada:", resultado)