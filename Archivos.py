import webbrowser

ruta = "prueba.html"

with open(ruta, mode="w", encoding="utf-8") as archivo:
    print("<!DOCTYPE html>", file = archivo)
    print('<html lang="es">', file = archivo)
    print("<head>", file = archivo)
    print(' <meta charset="utf-8">', file = archivo)
    print(" <title>HTML 5</title>", file = archivo)
    print(' <meta name="viewport" content="width=device-width, initial-scale=1.0">', file = archivo)
    print("</head>", file = archivo)
    print("", file = archivo)
    print("<body>", file = archivo)
    print(" <p>Esta página es una página HTML 5 válida.</p>", file = archivo)
    print("</body>", file = archivo)
    print("</html>", file = archivo)
    archivo.close()

webbrowser.open(ruta)

