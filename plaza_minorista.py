# plaza_minorista.py
from plaza_minorista import clasificar_temperatura
def clasificar_temperatura(promedio):
    if promedio < 4:
        return "Temperatura segura"
    elif 4 <= promedio <= 8:
        return "Temperatura en observación"
    else:
        return "Temperatura peligrosa"

mediciones = [2, 3, 5, 7, 9] * 20  # 100 mediciones
# Métodos de listas
mediciones.pop()  # eliminar última
posicion = mediciones.index(5)  # buscar posición
mediciones.pop(posicion)  # eliminar por posición

promedio = sum(mediciones) / len(mediciones)
print(f"Promedio: {promedio}")
print("Clasificación:", clasificar_temperatura(promedio))
