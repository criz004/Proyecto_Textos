from transformers import pipeline
import re

relleno = pipeline("fill-mask", model="dccuchile/bert-base-spanish-wwm-cased")

def corregir(texto):
    palabras = texto.split()
    sugerencias = {}

    for i, palabra in enumerate(palabras):
        # Heurística simple: detectar palabras "sospechosas"
        if not re.fullmatch(r"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ]+", palabra):
            continue  # saltar puntuación o números

        if len(palabra) < 3 or palabra.lower() in ["el", "la", "con", "a", "su", "va"]: 
            continue  # ignorar palabras muy cortas o comunes

        # Creamos la oración enmascarada
        enmascarada = palabras.copy()
        enmascarada[i] = "[MASK]"
        oracion = " ".join(enmascarada)

        resultados = relleno(oracion)
        if resultados:
            mejor = resultados[0]["token_str"]
            if mejor.lower() != palabra.lower():  # si la sugerencia es diferente
                sugerencias[palabra] = mejor

    return sugerencias

entrada = "el niñio va a la escueela con su peroo"
correcciones = corregir(entrada)

print("Texto original:", entrada)
print("Correcciones sugeridas:")
for incorrecta, sugerida in correcciones.items():
    print(f"- '{incorrecta}' → '{sugerida}'")
