from clases.player import Player
import json


def guardar_datos(players, archivo):
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump([p.to_dict() for p in players], f, indent=4, ensure_ascii=False)

def cargar_datos(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Player.from_dict(p) for p in data]
    except FileNotFoundError:
        return []