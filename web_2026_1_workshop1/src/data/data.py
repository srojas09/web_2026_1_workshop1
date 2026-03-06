class Data:

    def invertir_lista(self, lista):
        resultado = []
        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])
        return resultado

    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def eliminar_duplicados(self, lista):
        resultado = []

        for item in lista:
            existe = False
            for r in resultado:
                if r == item and type(r) == type(item):
                    existe = True
                    break
            if not existe:
                resultado.append(item)

        return resultado

    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i = j = 0

        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1

        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1

        return resultado

    def rotar_lista(self, lista, k):
        if not lista:
            return []

        n = len(lista)
        k = k % n

        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_real = 0
        for num in lista:
            suma_real += num
        return suma_esperada - suma_real

    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            encontrado = False
            for e in conjunto2:
                if e == elemento:
                    encontrado = True
                    break
            if not encontrado:
                return False
        return True

    def implementar_pila(self):
        pila = []

        def push(valor):
            pila.append(valor)

        def pop():
            if pila:
                return pila.pop()
            return None

        def peek():
            if pila:
                return pila[-1]
            return None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }

    def implementar_cola(self):
        cola = []

        def enqueue(valor):
            cola.append(valor)

        def dequeue():
            if cola:
                return cola.pop(0)
            return None

        def peek():
            if cola:
                return cola[0]
            return None

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }

    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []

        filas = len(matriz)
        columnas = len(matriz[0])

        transpuesta = []

        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            transpuesta.append(nueva_fila)

        return transpuesta