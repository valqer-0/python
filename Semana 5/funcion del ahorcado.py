import random

def obtener_ahorcado(errores):
    estados = [
        """
           ┌───────┐
           │       │
           │       
           │      
           │      
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │      
           │      
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │       │
           │      
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │      /│
           │      
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │      /│\\
           │      
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │      /│\\
           │      / 
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │      /│\\
           │      / \\
           │
        ═══╧═══════════
        """
    ]
    return estados[errores]

def mostrar_vidas(vidas_restantes, vidas_totales=6):
    corazones_llenos = "❤️ "*vidas_restantes
    corazones_vacios = "🖤 "*(vidas_totales - vidas_restantes)
    return corazones_llenos + corazones_vacios

def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jugar():
    palabras = [
        "python", "javascript", "programacion", "computadora", "algoritmo",
        "variable", "funcion", "bucle", "condicional", "estructura",
        "biblioteca", "modulo", "clase", "objeto", "herencia",
        "polimorfismo", "encapsulamiento", "compilador", "interprete"
    ]

    palabra = random.choice(palabras).upper()
    letras_adivinadas = set()
    letras_incorrectas = set()
    vidas_totales = 6
    vidas = vidas_totales
    errores = 0

    while True:
        print("\n" + "="*50)
        print("\t\t🎮 JUEGO DEL AHORCADO 🎮")
        print("="*50)

        print(obtener_ahorcado(errores))
        print()
        print(f"Vidas: {mostrar_vidas(vidas, vidas_totales)}")
        print(f"Palabra: {mostrar_palabra(palabra, letras_adivinadas)}")
        if letras_incorrectas:
            print(f"Letras incorrectas: {' '.join(sorted(letras_incorrectas))}")

        # Verificar victoria
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"\n¡Felicidades! Has adivinado la palabra: {palabra}")
            break

        # Verificar derrota
        if vidas <= 0:
            print(obtener_ahorcado(errores))
            print(f"\nHas perdido. La palabra era: {palabra}")
            break

        intento = input("Ingresa una letra o intenta adivinar la palabra completa: ").strip().upper()
        if not intento:
            print("Entrada vacía. Intenta de nuevo.")
            continue

        if len(intento) == 1:
            letra = intento
            if not letra.isalpha():
                print("Por favor ingresa una letra válida.")
                continue
            if letra in letras_adivinadas or letra in letras_incorrectas:
                print("Ya intentaste esa letra. Intenta otra.")
                continue
            if letra in palabra:
                letras_adivinadas.add(letra)
                print("¡Bien! La letra está en la palabra.")
            else:
                letras_incorrectas.add(letra)
                vidas -= 1
                errores += 1
                print("¡Uy! Esa letra no está.")
        else:
            # Intento adivinar la palabra completa
            if intento == palabra:
                print(f"\n¡Felicidades! Has adivinado la palabra: {palabra}")
                break
            else:
                vidas -= 1
                errores += 1
                print("No acertaste la palabra completa.")

    jugar_otra = input("\n¿Quieres jugar otra vez? (S/N): ").strip().upper()
    if jugar_otra == "S":
        jugar()
    else:
        print("Gracias por jugar. ¡Hasta luego!")


if __name__ == "__main__":
    jugar()