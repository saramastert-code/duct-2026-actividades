
import matplotlib.pyplot as plt


def leer_archivo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
        return texto

    except FileNotFoundError:
        print("Error: no se encontró el archivo.")
        return None


def contar_frecuencias(texto):
    palabras = texto.lower().split()
    frecuencias = {}

    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias


def generar_grafico(frecuencias):
    top_10 = sorted(
        frecuencias.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    palabras = [palabra for palabra, frecuencia in top_10]
    valores = [frecuencia for palabra, frecuencia in top_10]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title("Las 10 palabras más frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()

    plt.savefig("grafico_frecuencias.png", dpi=150)
    plt.show()


def main():
    ruta = "mercado_palabras.txt"

    texto = leer_archivo(ruta)

    if texto is None:
        return

    frecuencias = contar_frecuencias(texto)

    generar_grafico(frecuencias)


if __name__ == "__main__":
    main()
