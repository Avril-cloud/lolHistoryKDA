from datetime import datetime
class Partida:
    def __init__(self, campeon, kill, death, assist, farm, vision, fecha=None):
        self.campeon = campeon
        self.kill = kill
        self.death = death
        self.assist = assist
        self.farm = farm
        self.vision = vision
        self.fecha = fecha if fecha else datetime.now()

    def calcular_kda(self):
        if self.death == 0:
            return self.kill + self.assist
        return (self.kill + self.assist) / self.death
    
        


    def resumen_partida(self):
        return (
            f"Campeón: {self.campeon} | Fecha: {self.fecha.strftime('%d/%m/%Y')} | "
            f"Kills: {self.kill} | Deaths: {self.death} | Assists: {self.assist} | "
            f"Farm: {self.farm} | Visión: {self.vision} | KDA: {self.calcular_kda():.2f}"
        )

    def to_dict(self):
        return {
            "campeon": self.campeon,
            "kill": self.kill,
            "death": self.death,
            "assist": self.assist,
            "farm": self.farm,
            "vision": self.vision,
            "fecha": self.fecha.isoformat()
        }

    @staticmethod
    def from_dict(data):
        fecha = datetime.fromisoformat(data["fecha"])
        return Partida(
            campeon=data["campeon"],
            kill=data["kill"],
            death=data["death"],
            assist=data["assist"],
            farm=data["farm"],
            vision=data["vision"],
            fecha=fecha
        )
    
