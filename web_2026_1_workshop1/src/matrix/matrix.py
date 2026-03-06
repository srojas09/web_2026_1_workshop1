class Matrix:

    # -------------------------
    # VALIDACIÓN INTERNA
    # -------------------------

    def _es_matriz_valida(self, M):
        if not M or not isinstance(M, list):
            return False
        columnas = len(M[0])
        for fila in M:
            if not isinstance(fila, list) or len(fila) != columnas:
                return False
        return True


    # -------------------------
    # OPERACIONES BÁSICAS
    # -------------------------

    def suma_matrices(self, A, B):
        if not self._es_matriz_valida(A) or not self._es_matriz_valida(B):
            raise ValueError("Matriz inválida")
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Dimensiones incompatibles")
        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] + B[i][j])
            resultado.append(fila)
        return resultado

    def resta_matrices(self, A, B):
        if not self._es_matriz_valida(A) or not self._es_matriz_valida(B):
            raise ValueError("Matriz inválida")
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Dimensiones incompatibles")
        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] - B[i][j])
            resultado.append(fila)
        return resultado

    def multiplicar_matrices(self, A, B):
        if not self._es_matriz_valida(A) or not self._es_matriz_valida(B):
            raise ValueError("Matriz inválida")
        if len(A[0]) != len(B):
            raise ValueError("Dimensiones incompatibles")
        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(B[0])):
                suma = 0
                for k in range(len(B)):
                    suma += A[i][k] * B[k][j]
                fila.append(suma)
            resultado.append(fila)
        return resultado

    def multiplicar_escalar(self, matriz, escalar):
        if not self._es_matriz_valida(matriz):
            raise ValueError("Matriz inválida")
        resultado = []
        for fila in matriz:
            nueva_fila = []
            for elemento in fila:
                nueva_fila.append(elemento * escalar)
            resultado.append(nueva_fila)
        return resultado


    # -------------------------
    # PROPIEDADES
    # -------------------------

    def transpuesta(self, matriz):
        if not matriz:
            return []
        if not self._es_matriz_valida(matriz):
            raise ValueError("Matriz inválida")
        filas = len(matriz)
        columnas = len(matriz[0])
        resultado = []
        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            resultado.append(nueva_fila)
        return resultado

    def es_cuadrada(self, matriz):
        if not self._es_matriz_valida(matriz):
            return False
        return len(matriz) == len(matriz[0])

    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][j] != matriz[j][i]:
                    return False
        return True

    def traza(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("No es cuadrada")
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][i]
        return suma


    # -------------------------
    # DETERMINANTES
    # -------------------------

    def determinante_2x2(self, matriz):
        if not self._es_matriz_valida(matriz):
            raise ValueError("Matriz inválida")
        if len(matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("No es 2x2")
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    def determinante_3x3(self, M):
        if not self._es_matriz_valida(M) or len(M) != 3 or len(M[0]) != 3:
            raise ValueError("No es 3x3")

        a, b, c = M[0]
        d, e, f = M[1]
        g, h, i = M[2]

        return (
            a*(e*i - f*h) -
            b*(d*i - f*g) +
            c*(d*h - e*g)
        )


    # -------------------------
    # UTILIDADES
    # -------------------------

    def identidad(self, n):
        if n <= 0:
            return []
        resultado = []
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(1 if i == j else 0)
            resultado.append(fila)
        return resultado

    def diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("No es cuadrada")
        resultado = []
        for i in range(len(matriz)):
            resultado.append(matriz[i][i])
        return resultado

    def es_diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if i != j and matriz[i][j] != 0:
                    return False
        return True

    def rotar_90(self, matriz):
        if not self._es_matriz_valida(matriz):
            raise ValueError("Matriz inválida")
        filas = len(matriz)
        columnas = len(matriz[0])
        resultado = []
        for j in range(columnas):
            nueva_fila = []
            for i in range(filas - 1, -1, -1):
                nueva_fila.append(matriz[i][j])
            resultado.append(nueva_fila)
        return resultado

    def buscar_en_matriz(self, matriz, valor):
        if matriz == []:
            return []
        posiciones = []
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == valor:
                    posiciones.append((i, j))
        return posiciones