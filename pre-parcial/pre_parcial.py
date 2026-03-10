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






