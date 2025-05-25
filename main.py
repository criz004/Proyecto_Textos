import difflib
import json

# Banco de palabras correctas (puede expandirse)
with open("spanish_words.json", "r", encoding="utf-8") as f:
    banco_palabras = set(json.load(f))

with open("es_50k.txt", encoding="utf-8") as f:
    frecuentes = set(line.strip().split()[0] for line in f)

def corregir_texto(texto):
    palabras = texto.lower().split()
    correcciones = {}

    for palabra in palabras:
        if palabra not in banco_palabras:
            sugerencias = [
                s for s in difflib.get_close_matches(palabra, banco_palabras, n=5, cutoff=0.7)
                if s in frecuentes
            ]
            if sugerencias:
                correcciones[palabra] = sugerencias[0]

    return correcciones

# Ejemplo de uso
entrada = "el nino va a la escula con su peroo"
correcciones = corregir_texto(entrada)

print("Texto ingresado:", entrada)
print("Sugerencias de corrección:")
for palabra, sugerencia in correcciones.items():
    print(f"- '{palabra}' podría ser '{sugerencia}'")