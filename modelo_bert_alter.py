from transformers import pipeline

# Cargamos un modelo entrenado en español
relleno = pipeline("fill-mask", model="dccuchile/bert-base-spanish-wwm-cased")

# Texto con una palabra que vamos a evaluar
oracion = "el niño va a la [MASK] con su perro"

# Obtener sugerencias para la palabra faltante
resultados = relleno(oracion)

for r in resultados:
    if r['score'] > 0.2:
        # Filtramos las sugerencias con una confianza baja
        print(f"Sugerencia: {r['sequence']} (confianza: {r['score']:.4f})")
