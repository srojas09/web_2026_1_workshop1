import random

class Games:

    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        opciones = {"piedra", "papel", "tijera"}

        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"

        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }

        if reglas[jugador1] == jugador2:
            return "jugador1"
        else:
            return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        hay_espacios = any(" " in fila for fila in tablero)

        # Filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]

        # Columnas
        for i in range(3):
            if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
                return tablero[0][i]

        # Diagonales (solo si el tablero está completo)
        if not hay_espacios:
            if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
                return tablero[0][0]

            if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
                return tablero[0][2]

        if hay_espacios:
            return "continua"

        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, f1, c1, f2, c2, tablero):

        if not (0 <= f1 < 8 and 0 <= c1 < 8 and 0 <= f2 < 8 and 0 <= c2 < 8):
            return False

        if f1 == f2 and c1 == c2:
            return False

        if f1 != f2 and c1 != c2:
            return False

        # Movimiento horizontal
        if f1 == f2:
            paso = 1 if c2 > c1 else -1
            for c in range(c1 + paso, c2, paso):
                if tablero[f1][c] != " ":
                    return False

        # Movimiento vertical
        if c1 == c2:
            paso = 1 if f2 > f1 else -1
            for f in range(f1 + paso, f2, paso):
                if tablero[f][c1] != " ":
                    return False

        return True