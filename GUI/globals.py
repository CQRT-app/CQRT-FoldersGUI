import json

__author__ = "reza0310"


def initialize():
    # Variables indépendantes:

    global HEADER_LENGTH
    HEADER_LENGTH = 10

    global FPS
    FPS = 10

    global separateur
    separateur = "/"

    global aliases
    f = open("aliases.json", "r")
    aliases = json.load(f)
    f.close()

    global images
    images = {"arriere_plan": {
                                "path":".."+separateur+"DATA"+separateur+"background.jpg",
                                "url":"https://www.freepik.com/free-photo/background_3012025.htm#query=white%20background%20png&position=4&from_view=keyword&track=ais",
                                "author_name":"lifeforstock",
                                "author_url":"https://www.freepik.com/author/lifeforstock"
                               },
              "banniere": {
                                "path":".."+separateur+"DATA"+separateur+"black-smooth-textured-paper-background.jpg",
                                "url":"https://www.freepik.com/free-photo/black-smooth-textured-paper-background_13462566.htm#query=black&position=12&from_view=search&track=sph",
                                "author_name":"rawpixel.com",
                                "author_url":"https://www.freepik.com/author/rawpixel-com"
                               },
              "dossier": {
                                "path":".."+separateur+"DATA"+separateur+"dossier.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/dossier_1250635?term=dossier&page=1&position=24&origin=search&related_id=1250635",
                                "author_name":"Icongeek26",
                                "author_url":"https://www.flaticon.com/fr/auteurs/icongeek26"
                               },
              "nouveau_dossier": {
                                "path":".."+separateur+"DATA"+separateur+"nouveau-dossier.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/nouveau-dossier_9440110?term=nouveau+dossier&page=1&position=51&origin=search&related_id=9440110",
                                "author_name":"Radhe Icon",
                                "author_url":"https://www.flaticon.com/fr/auteurs/radhe-icon"
                               },
              "porte-clefs": {
                                "path":".."+separateur+"DATA"+separateur+"clefs.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/cles_11086755?term=porte-clefs&page=5&position=84&origin=search&related_id=11086755",
                                "author_name":"Creative Squad",
                                "author_url":"https://www.flaticon.com/fr/auteurs/creative-squad"
                               },
              "message_ferme": {
                                "path":".."+separateur+"DATA"+separateur+"enveloppe.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/enveloppe_126516?term=enveloppe&page=1&position=2&origin=search&related_id=126516",
                                "author_name":"Gregor Cresnar",
                                "author_url":"https://www.flaticon.com/fr/auteurs/gregor-cresnar"
                               },
              "message_ouvert": {
                                "path":".."+separateur+"DATA"+separateur+"ouvrir-le-courrier.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/ouvrir-le-courrier_488451?related_id=488451",
                                "author_name":"Freepik",
                                "author_url":"https://www.flaticon.com/fr/auteurs/freepik"
                               },
              "co_ok": {
                                "path":".."+separateur+"DATA"+separateur+"verifier.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/verifier_10901238?term=ok&page=1&position=26&origin=search&related_id=10901238",
                                "author_name":"Boris farias (modifié par Yann Duclos)",
                                "author_url":"https://www.flaticon.com/fr/auteurs/boris-farias"
                               },
              "co_ko": {
                                "path":".."+separateur+"DATA"+separateur+"proche.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/proche_3541897?term=croix&page=1&position=52&origin=search&related_id=3541897",
                                "author_name":"riajulislam (modifié par Yann Duclos)",
                                "author_url":"https://www.flaticon.com/fr/auteurs/riajulislam"
                               },
              "co_deco": {
                                "path":".."+separateur+"DATA"+separateur+"point-dinterrogation-dans-un-cercle-sombre.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/point-dinterrogation-dans-un-cercle-sombre_71768?term=dans+un+cercle&page=1&position=22&origin=search&related_id=71768",
                                "author_name":"Freepik (modifié par Yann Duclos)",
                                "author_url":"https://www.flaticon.com/fr/auteurs/freepik"
                               },
              "retour": {
                                "path":".."+separateur+"DATA"+separateur+"fleche-gauche.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/fleche-gauche_271218?term=fleche+arri%C3%A8re&page=1&position=18&origin=search&related_id=271218",
                                "author_name":"Roundicons",
                                "author_url":"https://www.flaticon.com/fr/auteurs/roundicons"
                               },
              "textinput": {
                                "path":"Framework-Kivy"+separateur+"framework_core"+separateur+"data"+separateur+"input.png",
                                "url":"https://github.com/reza0310/Framework-Kivy/blob/main/framework_core/data/input.png",
                                "author_name":"Unknown",
                                "author_url":"Unknown"
                               },
              "info": {
                                "path":".."+separateur+"DATA"+separateur+"information.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/information_545674?term=information&page=1&position=3&origin=search&related_id=545674",
                                "author_name":"Freepik (modifié par Yann Duclos)",
                                "author_url":"https://www.flaticon.com/fr/auteurs/freepik"
                               },
              "clefs": {
                                "path":".."+separateur+"DATA"+separateur+"cle.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/cle_2556639?term=clef&page=1&position=1&origin=search&related_id=2556639",
                                "author_name":"Indielogy",
                                "author_url":"https://www.flaticon.com/fr/auteurs/indielogy"
                               },
              "compte": {
                                "path":".."+separateur+"DATA"+separateur+"compte.png",
                                "url":"https://www.flaticon.com/fr/icone-gratuite/compte_2207595?term=compte&page=1&position=1&origin=search&related_id=2207595",
                                "author_name":"mattbadal",
                                "author_url":"https://www.flaticon.com/fr/auteurs/mattbadal"
                               }
              }

    global mode
    mode = "DEV"

    global longueur_dev
    longueur_dev = 1080

    global largeur_dev
    largeur_dev = 720

    global orientation
    orientation = "paysage"
    
    global actuel
    actuel = "../CQRT-algo/CLIENT/home"
    
    global racine
    racine = "../CQRT-algo/CLIENT/home"

    # Dépendances:
    from framework import HUD
    from CQRT import Coeur
    from structures import Client

    # Variables dépendates:

    global hud
    hud = HUD()

    global jeu
    jeu = Coeur()

    global account_client
    account_client = Client()

    global message_client
    message_client = Client()

    global sync_client
    sync_client = Client()