from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class pokemon(BaseModel):
    id:int
    name:str
    attack:int
    live:int
    type:str

df=pd.read_csv("pokemons.csv")

pokemons=df.to_dict(orient="records")

@app.get("/showallpokemons")
def show_all_pokemon():
    return pokemons

@app.get("/onepokemon/{name}")
def show_one_pokemon(name: str):
    pokemon = df[df["name"].str.lower() == name.lower()]
    return pokemon.to_dict(orient="records")

@app.get("/onepokemonbyid/{id}")
def show_one_pokemon(id: int):
    pokemon = df[df["id"] == id]
    return pokemon.to_dict(orient="records")

@app.get("/battle/{pokemon1}/{pokemon2}")
def pokemon_battle(pokemon1: str, pokemon2: str):

    p1 = df[df["name"].str.lower() == pokemon1.lower()].iloc[0]
    p2 = df[df["name"].str.lower() == pokemon2.lower()].iloc[0]

    life1 = int(p1["live"])
    life2 = int(p2["live"])

    attack1 = int(p1["attack"])
    attack2 = int(p2["attack"])

    log = []

    log.append({
        "pokemon1": p1["name"],
        "attack": attack1,
        "life": life1,
        "type": p1["type"]
    })

    log.append({
        "pokemon2": p2["name"],
        "attack": attack2,
        "life": life2,
        "type": p2["type"]
    })

    while life1 > 0 and life2 > 0:

        life2 -= attack1
        log.append(f"{p1['name']} attacks {p2['name']} - remaining life: {p2['name']} live: {max(life2,0)}")

        if life2 <= 0:
            return {"winner": p1["name"], "battle_log": log}

        life1 -= attack2
        log.append(f"{p2['name']} attacks {p1['name']} - remaining life: {p1['name']} live: {max(life1,0)}")

        if life1 <= 0:
            return {"winner": p2["name"], "battle_log": log}

@app.get("/orderby/{column}")
def pokemon_orderby(column: str, desc: bool=False):
    ordered = df.sort_values(by=column, ascending=not desc)
    return ordered.to_dict(orient="records")








