import random
from random import randrange

def iniciarJuego():
    j1 = random.randint(1,6)
    j2 = random.randint(1,6)

    print(f"\nEl jugador 1 obtuvo {j1} puntos")
    print(f"\nEl jugador 2 obtuvo {j2} puntos")

    if j1>j2:
        print("\nEl ganador es el jugador 1")
    elif j1==j2:
        print("\nHubo un empate")
    else:
        print("\nEl ganador es el jugador 2")

def main():
    iniciarJuego()

if __name__ == "__main__":
    main()