class Strings:

    def es_palindromo(self, texto):
        texto_limpio = ""
        for c in texto.lower():
            if c.isalnum():
                texto_limpio += c
        invertido = ""
        for c in texto_limpio:
            invertido = c + invertido
        return texto_limpio == invertido

    def invertir_cadena(self, texto):
        resultado = ""
        for c in texto:
            resultado = c + resultado
        return resultado

    def contar_vocales(self, texto):
        vocales = "aeiou"
        contador = 0
        for c in texto.lower():
            if c in vocales:
                contador += 1
        return contador

    def contar_consonantes(self, texto):
        vocales = "aeiou"
        contador = 0
        for caracter in texto.lower():
            if caracter.isalpha() and caracter not in vocales:
                contador += 1
        return contador

    def es_anagrama(self, texto1, texto2):
        limpio1 = ""
        limpio2 = ""
        for c in texto1.lower():
            if c.isalnum():
                limpio1 += c
        for c in texto2.lower():
            if c.isalnum():
                limpio2 += c
        return sorted(limpio1) == sorted(limpio2)

    def contar_palabras(self, texto):
        palabras = texto.strip().split()
        return len(palabras)

    def palabras_mayus(self, texto):
        resultado = ""
        nueva_palabra = True
        for c in texto:
            if c == " ":
                resultado += c
                nueva_palabra = True
            else:
                if nueva_palabra:
                    resultado += c.upper()
                    nueva_palabra = False
                else:
                    resultado += c.lower()
        return resultado

    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        espacio_anterior = False
        for c in texto:
            if c == " ":
                if not espacio_anterior:
                    resultado += c
                espacio_anterior = True
            else:
                resultado += c
                espacio_anterior = False
        return resultado

    def es_numero_entero(self, texto):
        if texto == "":
            return False
        if texto[0] in "+-":
            if len(texto) == 1:
                return False
            texto = texto[1:]
        for c in texto:
            if c < '0' or c > '9':
                return False
        return True

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord('a') if c.islower() else ord('A')
                nueva = (ord(c) - base + desplazamiento) % 26
                resultado += chr(base + nueva)
            else:
                resultado += c
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        if subcadena == "":
            return []
        posiciones = []
        n = len(texto)
        m = len(subcadena)
        for i in range(n - m + 1):
            coincide = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    coincide = False
                    break
            if coincide:
                posiciones.append(i)
        return posiciones