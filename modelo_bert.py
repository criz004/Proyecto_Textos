from transformers import pipeline

# Cargamos un modelo entrenado en español
relleno = pipeline("fill-mask", model="dccuchile/bert-base-spanish-wwm-cased")

# Texto con una palabra que vamos a evaluar
oracion = "el niño va a la [MASK] con su perro"

# Obtener sugerencias para la palabra faltante
resultados = relleno(oracion)

for r in resultados:
    print(f"Sugerencia: {r['sequence']} (confianza: {r['score']:.4f})")
