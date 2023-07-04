__author__ = "reza0310"

from kivy.clock import Clock

from random import randint
from structures import Commandeur
import framework
import globals


class Coeur:

    def initialiser(self):
        self.commandeur = Commandeur()
        self.event = Clock.schedule_interval(self.actualiser, 1/globals.FPS)  # 60 fps

    def actualiser(self, dt):
        globals.hud.image(500, 450, 1000, 900, globals.images["arriere_plan"]["path"])
        globals.hud.image(500, 950, 1000, 100, globals.images["banniere"]["path"])
        globals.hud.image(50, 950, 100, 100, globals.images["retour"]["path"])
        globals.hud.image(250, 950, 100, 100, globals.images["co_ok"]["path"])
        globals.hud.image(500, 950, 100, 100, globals.images["co_ok"]["path"])
        globals.hud.image(750, 950, 100, 100, globals.images["co_ok"]["path"])
        globals.hud.image(950, 950, 100, 100, globals.images["nouveau_dossier"]["path"])
        x = 0
        y = 800
        for res in self.commandeur.send("ls"):
            globals.hud.image(x+globals.hud.longueur//15, y+globals.hud.largeur//15, 100, 100, globals.images[res["type"].lower()]["path"])
            globals.hud.texte(x+globals.hud.longueur//18, y-globals.hud.largeur//80, res["nom"], color=(0, 0, 0, 1))
            x += 100
            y += x//950
            x %= 950
            
            