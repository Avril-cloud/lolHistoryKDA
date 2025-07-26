
from clases.partida import Partida


class Player:
    def __init__(self, nick, elo,):
        self.nick = nick
        self.elo = elo
        self.historial_partidas = []
    
    def agregar_partida(self, partida):
        self.historial_partidas.append(partida)

    def promedio_kda(self):
        if not self.historial_partidas:
            return 0
        total_kda = 0

        for partida in self.historial_partidas:
            total_kda += partida.calcular_kda()
        
        promedio = total_kda / len(self.historial_partidas)

        return promedio

    def resumen_historial(self):
        if not self.historial_partidas:
            return f"{self.nick} no tiene partidas registradas."
        resumenes = [partida.resumen_partida() for partida in self.historial_partidas]
        resumen = f"Historial de partidas de {self.nick} (Elo: {self.elo}):\n"
        resumen += "-" * 60 + "\n"
        resumen += "\n".join(resumenes) + "\n"
        resumen += "-" * 60 + "\n"
        resumen += f"Promedio de KDA: {self.promedio_kda():.2f}"
        return resumen

    def to_dict(self):
        return {
            "nick": self.nick,
            "elo": self.elo,
            "historial_partidas": [p.to_dict() for p in self.historial_partidas]
        }
    
    @staticmethod
    def from_dict(data):
        player = Player(data["nick"], data["elo"])
        player.historial_partidas = [Partida.from_dict(p) for p in data["historial_partidas"]]
        return player