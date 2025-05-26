import language_tool_python

# Conectarse a la API pública
tool = language_tool_python.LanguageToolPublicAPI('es')

texto = "el nino va a la escula con su peroo"
matches = tool.check(texto)

for m in matches:
    print(f"{m.context} → {m.message} | Sugerencias: {m.replacements}")
