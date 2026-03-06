class Stats:
    def promedio(self, numeros):
        if len(numeros) == 0:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        if len(numeros) == 0:
            return 0
        
        nums = sorted(numeros)
        n = len(nums)
        mitad = n // 2
        
        if n % 2 == 1:
            return float(nums[mitad])
        else:
            return (nums[mitad - 1] + nums[mitad]) / 2
    
    def moda(self, numeros):
        frecuencias = {}
        for num in numeros:
            if num in frecuencias:
                frecuencias[num] += 1
            else:
                frecuencias[num] = 1
        
        max_frecuencia = 0
        moda = None
        
        for num in numeros:  # mantiene orden de aparición
            if frecuencias[num] > max_frecuencia:
                max_frecuencia = frecuencias[num]
                moda = num
        
        return moda
    
    def desviacion_estandar(self, numeros):
        if len(numeros) == 0:
            return 0
        
        media = self.promedio(numeros)
        suma = 0
        
        for num in numeros:
            suma += (num - media) ** 2
        
        varianza = suma / len(numeros)  # poblacional
        return varianza ** 0.5
    
    def varianza(self, numeros):
        if len(numeros) == 0:
            return 0
        
        media = self.promedio(numeros)
        suma = 0
        
        for num in numeros:
            suma += (num - media) ** 2
        
        return suma / len(numeros)
    
    def rango(self, numeros):
        if len(numeros) == 0:
            return 0
        return max(numeros) - min(numeros)