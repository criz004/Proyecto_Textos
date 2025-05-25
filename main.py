import difflib
import json
import spacy

# Cargar el modelo de lenguaje español
nlp = spacy.load("es_core_news_sm")

# Banco de palabras usando un archivo JSON
with open("spanish_words.json", "r", encoding="utf-8") as f:
    banco_palabras = set(json.load(f))

with open("es_50k.txt", encoding="utf-8") as f:
    frecuentes = set(line.strip().split()[0] for line in f)

# Función para corregir texto
def corregir_texto(texto):
    doc = nlp(texto.lower())
    correcciones = {}

    for token in doc:
        palabra = token.text
        if not palabra.isalpha():
            continue
        if palabra not in banco_palabras:
            # Buscar sugerencias fonéticamente parecidas
            sugerencias = difflib.get_close_matches(palabra, banco_palabras, n=10, cutoff=0.7)
            # Filtrar por frecuencia y por tipo de palabra (POS)
            sugerencias_filtradas = [
                s for s in sugerencias
                if s in frecuentes and nlp(s)[0].pos_ == token.pos_
            ]
            if sugerencias_filtradas:
                correcciones[palabra] = sugerencias_filtradas[0]

    return correcciones

# Ejemplo de uso
entrada = "el nino va a la escula con su peroo"
correcciones = corregir_texto(entrada)

print("Texto ingresado:", entrada)
print("Sugerencias de corrección:")
for palabra, sugerencia in correcciones.items():
    print(f"- '{palabra}' podría ser '{sugerencia}'")