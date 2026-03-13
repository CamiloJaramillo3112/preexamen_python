# epm_consumo.py
from epm_consumo import clasificar_consumo

def clasificar_consumo(promedio):
    if promedio < 30:
        return "Alerta por bajo nivel"
    elif 30 <= promedio <= 70:
        return "Consumo estable"
    else:
        return "Consumo alto (abrir compuertas)"

lecturas = [20, 40, 60, 80, 100] * 4  # 20 lecturas
promedio = sum(lecturas) / len(lecturas)
print(f"Promedio: {promedio}")
print("Clasificación:", clasificar_consumo(promedio))
