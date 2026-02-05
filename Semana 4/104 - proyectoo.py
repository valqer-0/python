import random

def juego_adivinar():
    nombre = input("¿Cuál es tu nombre? ").strip() or "Jugador"
    secreto = random.randint(1, 100)
    intentos_max = 8
    intentos = 0

    print(f"\nBueno, {nombre}, he pensado un número entre 1 y 100. Tienes {intentos_max} intentos para adivinarlo.\n")

    while intentos < intentos_max:
        try:
            intento = int(input(f"Intento {intentos+1}/{intentos_max}. Ingresa un número: "))
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.\n")
            continue

        if intento < 1 or intento > 100:
            print("Número no permitido. Debe estar entre 1 y 100.\n")
            continue

        intentos += 1

        if intento == secreto:
            print(f"¡Felicidades, {nombre}! Adivinaste el número en {intentos} intento(s).")
            break
        elif intento < secreto:
            print("Incorrecto: elegiste un número menor al secreto.\n")
        else:
            print("Incorrecto: elegiste un número mayor al secreto.\n")
    else:
        print(f"Se han agotado los {intentos_max} intentos. El número secreto era {secreto}. Buen intento.")

if __name__ == "__main__":
    juego_adivinar()