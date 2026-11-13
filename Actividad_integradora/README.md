# Analizador de texto

Este programa analiza un archivo de texto y cuenta la frecuencia de aparición de cada palabra utilizando un diccionario de Python.

Genera un gráfico de barras horizontales con las 10 palabras más frecuentes y lo guarda como `grafico_frecuencias.png`.

**Bibliotecas necesarias:**
- Python 3
- Matplotlib (`pip install matplotlib`)

**Ejecución:**

1. Guardar el archivo `mercado_palabras.txt` en la misma carpeta que el script.
2. Ejecutar en la terminal: `python analizador.py`.

Si el archivo de texto no existe, el programa informa el error mediante `try/except`.