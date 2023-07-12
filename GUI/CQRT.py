__author__ = "reza0310"

from kivy.clock import Clock
import threading
from random import randint
import json

from structures import Commandeur
import framework
import globals
from utils import *


class Coeur:

    def initialiser(self):
        self.commandeur = Commandeur()
        self.message = ""
        self.status_1 = ""
        self.status_2 = ""
        self.status_3 = ""
        self.status()
        self.input = framework.TextInput(500, 75, 800, 50, "Entrez vos commandes ici", textcolor=(0, 0, 0, 1))
        self.input.event.cancel()
        self.event = Clock.schedule_interval(self.actualiser, 1/globals.FPS)  # 60 fps
        self.status_update = Clock.schedule_interval(self.wrapper, 5)

    def wrapper(self, *dt):
        threading.Thread(target=self.status).start()

    def status(self, *dt):
        clients = [globals.account_client, globals.message_client, globals.sync_client]
        images = []
        for client in clients:
            if client.ip == "":
                images.append(globals.images["co_deco"]["path"])
            else:
                p = threading.Thread(target=client.ping)
                p.start()
                p.join(2)
                if p.is_alive():
                    p.kill()
                    images.append(globals.images["co_ko"]["path"])
                else:
                    images.append(globals.images["co_ok"]["path"])
                
        self.status_1, self.status_2, self.status_3 = images

    def set_msg(self, val):
        self.message = val
        self.switch('message')

    def banniere(self):
        globals.hud.unbind()
        
        globals.hud.image(500, 450, 1000, 900, globals.images["arriere_plan"]["path"])
        globals.hud.image(500, 950, 1000, 100, globals.images["banniere"]["path"])
        globals.hud.image(50, 950, 100, 100, globals.images["retour"]["path"])
        globals.hud.image(250, 950, 100, 100, self.status_1)
        globals.hud.image(500, 950, 100, 100, self.status_2)
        globals.hud.image(750, 950, 100, 100, self.status_3)
        globals.hud.image(950, 950, 100, 100, globals.images["info"]["path"])

    def actualiser(self, dt):
        self.banniere()
        
        globals.hud.image(500, 75, 800, 50, globals.images["banniere"]["path"])
        globals.hud.bind(self.input.x, self.input.y, self.input.tx, self.input.ty, self.input.action)
        self.input.actualiser(12)
        if self.input.sent:
            self.input.shown_text = self.commandeur.send(self.input.text)
            self.input.sent = False
        
        globals.hud.bind(50, 950, 100, 100, "globals.jeu.commandeur.send('cd ..')")
        globals.hud.bind(950, 950, 100, 100, "globals.jeu.switch('info')")
        x = 0
        y = 800
        for res in self.commandeur.send("ls"):
            if res["type"] == "MESSAGE":
                f = open(res["total"], "r")
                data = json.load(f)
                f.close()
                if "lu" not in data.keys():
                    data["lu"] = False
                    f = open(res["total"], "w")
                    json.dump(data, f)
                    f.close()
                globals.hud.image(x+globals.hud.longueur//15, y+globals.hud.largeur//15, 100, 100, globals.images["message_ouvert"]["path"] if data["lu"] else globals.images["message_ferme"]["path"])
                globals.hud.bind(x+globals.hud.longueur//15, y+globals.hud.largeur//15, 100, 100, f"globals.jeu.set_msg('{res['nom']}')")
            else:
                globals.hud.image(x+globals.hud.longueur//15, y+globals.hud.largeur//15, 100, 100, globals.images[res["type"].lower()]["path"])
                if res["type"] == "DOSSIER":
                    globals.hud.bind(x+globals.hud.longueur//15, y+globals.hud.largeur//15, 100, 100, f"globals.jeu.commandeur.send('cd {res['nom']}')")
            globals.hud.texte(x+globals.hud.longueur//15, y-globals.hud.largeur//60, res["nom"], color=(0, 0, 0, 1), centrer=True)
            x += 150
            y += x//950
            x %= 950
        globals.hud.texte(500, 20, self.commandeur.send("cwd")[21:], color=(0, 0, 0, 1), centrer=True)

    def infos(self, dt):
        self.banniere()
        
        globals.hud.bind(50, 950, 100, 100, "globals.jeu.switch('menu')")
        globals.hud.bind(950, 950, 100, 100, "globals.jeu.switch('credit')")
        y = 800
        globals.hud.texte(500, 870, "LISTE DES COMMANDES:", taille_police=30, centrer=True, color=(0, 0, 0, 1))
        res = self.commandeur.send("help")[0]
        for r in res.keys():
            texte = r + " = " + res[r]
            length = 155
            for i in range(0, len(texte), length):
                globals.hud.texte(10, y, texte[i:i+length], color=(0, 0, 0, 1))
                y -= 20

    def credits(self, dt):
        self.banniere()
        
        globals.hud.bind(50, 950, 100, 100, "globals.jeu.switch('info')")
        globals.hud.bind(950, 950, 100, 100, "globals.jeu.switch('menu')")
        globals.hud.texte(500, 870, "CREDITS:", taille_police=30, centrer=True, color=(0, 0, 0, 1))
        res = self.commandeur.send("credits")
        res[2]["Design interface"].append("reza0310")
        res[2]["Implémentation interface"].append("reza0310")
        for x in globals.images.keys():
            nom = globals.images[x]["author_name"]
            if nom not in res[2]["Ressources pour l'interface"] and nom != "Unknown":
                res[2]["Ressources pour l'interface"].append(nom)
        x = 125
        for categorie in res:
            y = 820
            for role in categorie.keys():
                y -= 30
                globals.hud.texte(x, y, role+":", taille_police=20, centrer=True, color=(0, 0, 0, 1))
                y -= 30
                for nom in categorie[role]:
                    length = 40
                    texte = nom
                    for i in range(0, len(texte), length):
                        globals.hud.texte(x, y, texte[i:i+length], centrer=True, color=(0, 0, 0, 1))
                        y -= 20
            x += 250

    def lire(self, dt):
        self.banniere()
        
        globals.hud.bind(50, 950, 100, 100, "globals.jeu.switch('menu')")
        globals.hud.bind(950, 950, 100, 100, "globals.jeu.switch('info')")
        res = self.message
        if type(res) == str:
            self.switch("menu")
        else:
            res = res[0]
            y = 800
            globals.hud.texte(500, 870, res["titre"], taille_police=30, centrer=True, color=(0, 0, 0, 1))
            for r in res.keys():
                texte = r + " = " + str(res[r])
                length = 155
                for i in range(0, len(texte), length):
                    globals.hud.texte(10, y, texte[i:i+length], color=(0, 0, 0, 1))
                    y -= 20

    def switch(self, menu):
        self.event.cancel()
        if menu == "menu":
            self.input = framework.TextInput(500, 75, 800, 50, "Entrez vos commandes ici", textcolor=(0, 0, 0, 1))
            self.input.event.cancel()
            self.event = Clock.schedule_interval(self.actualiser, 1/globals.FPS)
        elif menu == "info":
            self.event = Clock.schedule_interval(self.infos, 1/globals.FPS)
        elif menu == "credit":
            self.event = Clock.schedule_interval(self.credits, 1/globals.FPS)
        elif menu == "message":
            # On marque comme lu
            f = open(globals.actuel+globals.separateur+identifile_plus(self.message)[0], "r")
            message_data = json.load(f)
            f.close()
            message_data["lu"] = True
            f = open(globals.actuel+globals.separateur+identifile_plus(self.message)[0], "w")
            json.dump(message_data, f)
            f.close()
            # On précharge
            self.message = self.commandeur.send(f"read_message {self.message}")
            # On envoie
            self.event = Clock.schedule_interval(self.lire, 1/globals.FPS)
            
            