class Magic:

    def fibonacci(self, n):
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        
        resultado = []
        for i in range(n):
            resultado.append(self.fibonacci(i))
        return resultado

    def es_primo(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def generar_primos(self, n):
        primos = []
        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)
        return primos

    def es_numero_perfecto(self, n):
        if n <= 1:
            return False
        
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        
        return suma == n

    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        if n < 0:
            return None

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        n = abs(n)
        suma = 0
        while n > 0:
            suma += n % 10
            n //= 10
        return suma

    def es_numero_armstrong(self, n):
        num_str = str(abs(n))
        potencia = len(num_str)
        suma = 0
        
        for digito in num_str:
            suma += int(digito) ** potencia
        
        return suma == n

    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        
        if n == 0 or any(len(fila) != n for fila in matriz):
            return False
        
        suma_objetivo = sum(matriz[0])
        
        # filas
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        
        # columnas
        for col in range(n):
            suma_col = 0
            for fila in range(n):
                suma_col += matriz[fila][col]
            if suma_col != suma_objetivo:
                return False
        
        # diagonal principal
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        
        # diagonal secundaria
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False
        
        return True