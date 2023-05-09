# lista_config = (
#     "jugadas",
#     "victorias",
#     "dibujos"
# )

import random
from config_pptls import lista_config

jugadas = lista_config[0]
victorias = lista_config[1]
dibujos = lista_config[2]

# devuelve una de las jugadas
def pideUnNum():
    msg = "Dame un num: "
    entrada = ''
    invalido = False
    while not entrada.isnumeric():
        if invalido:
            print("Obligatoriamente debe ser un número")
        invalido = True
        entrada = input(msg)
    return int(entrada)

def elegirJugada():

    def imprime_lista():
        contador = 0
        for jugada in jugadas:
            print(f"{contador} - {jugada}")
            contador += 1

    def indice_valido_en_lista():
        jugada = None
        invalido = False
        while jugada not in range(len(jugadas)):
            if invalido:
                print("Elije una jugada válida")
            invalido = True
            jugada = pideUnNum()

        return jugada

    imprime_lista()

    return indice_valido_en_lista()

def aleatorizarJugada():
    return random.randrange(len(jugadas))

def imprimir(dibujo):
    for linea in dibujo:
        print(linea)

def decidirGanador(jugada0, jugada1):
    if jugada1 in victorias[jugada0]:
        return True

    return False


def mostrarEmpate(jugada):
    print(f"Habeis emptadao, los dos habéis elegido: {jugadas[jugada]}")
    imprimir(dibujos[jugada])

def mostrarVictoria(msg, jugada0, jugada1):
    print()
    print(msg)
    print(f"jugador 0  : {jugadas[jugada0]}")
    imprimir(dibujos[jugada0])
    print()
    print(f"jugador 1 : {jugadas[jugada1]}")
    imprimir(dibujos[jugada1])

def juego(vsCpu):
    jugada0 = aleatorizarJugada() if vsCpu else elegirJugada()
    jugada1 = aleatorizarJugada()


    ganador = None

    if jugada0 == jugada1:
        mostrarEmpate(jugada0)
    else:
        ganador = decidirGanador(jugada0, jugada1)
        msg = "GANA EL JUGADOR: " + "1" if ganador else "0"
        mostrarVictoria(msg, jugada0, jugada1)

    return ganador


def main():
    print("Elige, <=0 jugar una partida, >0 partidas automaticas")
    num = pideUnNum()
    if num <= 0:
        juego(False)
    else:
        contador = 0
        for partida in range(num):
            contador += 1 if juego(True) else 0

        print(f"Victorias: {contador}/{num}")
    print()

main()
