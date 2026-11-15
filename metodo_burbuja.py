def burbuja(arr):
    n = len(arr)
    # Optimización: si en una pasada no hubo intercambios, la lista ya está ordenada
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
        if not intercambiado:
            break
    return arr

# --- Ejercicio de prueba ---
if __name__ == "__main__":
    datos_burbuja = [64, 34, 25, 12, 22, 11, 90]
    print("--- Método de Burbuja ---")
    print("Lista original:", datos_burbuja)
    resultado = burbuja(datos_burbuja)
    print("Lista ordenada:", resultado)