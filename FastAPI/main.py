from datetime import datetime
import socket
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Caballero(BaseModel):
    id:int
    nombre:str
    constelacion:str
    vida:int=100
    armadora:bool = False
    cosmos:int

c1  = Caballero(id=1,  nombre="mu",              constelacion="aries",     cosmos=100)
c2  = Caballero(id=2,  nombre="aldebaran",       constelacion="tauro",     cosmos=100, armadora=True)
c3  = Caballero(id=3,  nombre="saga",            constelacion="geminis",   cosmos=100)
c4  = Caballero(id=4,  nombre="mascarademuerte", constelacion="cancer",    cosmos=100)
c5  = Caballero(id=5,  nombre="aioria",          constelacion="leo",       cosmos=100)
c6  = Caballero(id=6,  nombre="shaka",           constelacion="virgo",     cosmos=100)
c7  = Caballero(id=7,  nombre="dohko",           constelacion="libra",     cosmos=100)
c8  = Caballero(id=8,  nombre="milo",            constelacion="escorpio",  cosmos=100)
c9  = Caballero(id=9,  nombre="aioros",          constelacion="sagitario", cosmos=100)
c10 = Caballero(id=10, nombre="shura",           constelacion="capricornio", cosmos=100)
c11 = Caballero(id=11, nombre="camus",           constelacion="acuario",   cosmos=100)
c12 = Caballero(id=12, nombre="afrodita",        constelacion="piscis",    cosmos=100)

caballeros: list[Caballero] = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]


new_caballeros=[{"mu":"aries"},{"aldebaran":"tauro"},{"saga":"geminis"},{"mascarademuerte":"cancer"},
                {"aioria":"leo"},{"shaka":"virgo"},{"dohko":"libra"},{"milo":"escorpio"},{"aioros":"sagitario"},
                {"shura":"capricornio"},{"camus":"acuario"},{"afrodita":"piscis"}]

@app.get("/onecaballero/")
def show_one_caballero(i:int):
    return caballeros[i]

@app.get("/newcaballeros/")
def show_new_caballeros(inicio:int=0, fin:int=4):
    return caballeros[inicio:inicio+fin]

@app.get("/holanda")
def hello():
    return{"Hello":"in FastAPI"}

@app.get("/hola")
def Saludo():
    return{"Hello":socket.gethostname()}

@app.get("/sumar/{a}/{b}")
def sumar(a,b):
    res = int(a) + int(b)
    return{"resultado":res}

@app.get("/concat/{a}/{b}")
def concat(a,b):
    res = a +" "+ b
    return{"resultado":res}

#Construir un enpoint que reciba nombre y año de nacimiento
#debe retornar el nombre y la edad

@app.get("/edad/{name}/{year}")
def edad(name:str,year:int):
    year_now = datetime.now().year
    edad = year_now - year
    
    return {
        "nombre": name,
        "edad": edad
    }