from rich.console import Console 
from rich.table import Table
from clases.partida import Partida
console = Console()
from datetime import datetime

class Player:
    def __init__(self, nick, elo,):
        self.nick = nick
        self.elo = elo
        self.historial_partidas = []
    
    def agregar_partida(self, partida):
        self.historial_partidas.append(partida)
    
    def limpiar_partida(self):
        self.historial_partidas.clear()

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
            console.print("Este jugador no tiene partidas registradas.", style="red") 
            return
        console.print(f"\n [bold]Historial de {self.nick}(Elo: {self.elo})[/bold]")

        table = Table(show_header=True, header_style="medium_violet_red")

        table.add_column("Fecha")
        table.add_column("Campeón")
        table.add_column("Kills")
        table.add_column("Deaths")
        table.add_column("Assists")
        table.add_column("Farm")
        table.add_column("Visión")
        table.add_column("KDA")

        for partida in self.historial_partidas:
            table.add_row(
                partida.fecha.strftime('%d/%m/%Y'),
                partida.campeon,
                str(partida.kill),
                str(partida.death),
                str(partida.assist),
                str(partida.farm),
                str(partida.vision),
                f"{partida.calcular_kda():.2f}"
            )
        console.print(table)  

    def partidas_por_fecha(self, fecha_str):
        try:
            fecha_deseada = datetime.strptime(fecha_str, "%d/%m/%Y").date()
        except ValueError:
            console.print("[bold red]Formato de fecha inválido. Usá dd/mm/yyyy[/bold red]")
            return []
        return [p for p in self.historial_partidas if p.fecha.date() == fecha_deseada]

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