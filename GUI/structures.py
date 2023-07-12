__author__ = "reza0310"

import commandes
import utils
import cypher
import connexions
import globals
import socket
import time


class Commandeur():

    def __init__(self):
        self.commandes = {"help": commandes.help,
                          "h": commandes.help,
                          "?": commandes.help,
                          "cwd": commandes.cwd,
                          "ls": commandes.ls,
                          "listdir": commandes.ls,
                          "dir": commandes.ls,
                          "mkdir": commandes.mkdir,
                          "cd": commandes.cd,
                          "mkr": commandes.mkr,
                          "rm": commandes.rm,
                          "mv": commandes.mv,
                          "lkr": commandes.lkr,
                          "rsa_gen_keys": cypher.rsa_gen_keys,
                          "rgk": cypher.rsa_gen_keys,
                          "client_connect": connexions.client_connect,
                          "make_account": connexions.make_account,
                          "list_accounts": connexions.list_accounts,
                          "get_account": connexions.get_account,
                          "send_message": connexions.send_message,
                          "pull_messages": connexions.pull_messages,
                          "read_message": connexions.read_message,
                          "reset": commandes.reset,
                          "credits": commandes.credits,
                          "add_alias": commandes.add_alias,
                          "remove_alias": commandes.remove_alias,
                          "set_aliases": commandes.set_aliases,
                          "get_aliases": commandes.get_aliases}

    def send(self, commande):
        if commande == "quit":
            framework.stop()
        if commande in globals.aliases:
            commande = globals.aliases[commande]
        commande = commande.split('"')
        x = []
        for i in range(len(commande)):
            if i%2 == 0:
                for part in commande[i].split(" "):
                    x.append(part)
            else:
                x.append(commande[i])
        # Nettoyage
        while "" in x:
            x.remove("")
        # Analyse de la commande
        if x[0] not in self.commandes.keys():
            print("Command not found !")
        else:
            kwargs = {}
            i = 1
            while i < len(x):
                if x[i][0:2] == "--":
                    if i == len(x)-1 or x[i+1][0:2] == "--":
                        kwargs[x[i][2:]] = True
                    else:
                        kwargs[x[i][2:]] = x[i+1]
                        x.pop(i+1)
                    x.pop(i)
                    i -= 1
                i += 1
            try:
                return self.commandes[x[0]](*x[1:], **kwargs)
            except Exception as e:
                print("Bad arguments:", e)


class Client():

    def __init__(self):
        self.coeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ""
        self.port = 0
        self.occupe = False

    def connect(self, iport):
        ip, port = iport.split(":")
        port = int(port)
        self.coeur.connect((ip, port))
        self.ip = ip
        self.port = port
        return "."

    def echanger(self, message):  # Code pour envoyer un msg
        self.occupe = True
        print("Envoi de:", message.split("\0"))
        message = message.encode('utf-8')
        message_header = f"{len(message):<{globals.HEADER_LENGTH}}".encode('utf-8')
        self.coeur.send(message_header + message)
        message_header = self.coeur.recv(globals.HEADER_LENGTH)
        if not len(message_header):
            print('Connection perdue.')
        message_length = int(message_header.decode('utf-8').strip())
        time.sleep(1)
        message = self.coeur.recv(message_length).decode('utf-8')
        self.occupe = False
        return message.replace("&apos;", "'").replace('&quot;', '"')

    def ping(self):
        if self.occupe:
            return True
        message = "ping".encode('utf-8')
        message_header = f"{len(message):<{globals.HEADER_LENGTH}}".encode('utf-8')
        self.coeur.send(message_header + message)
        message_header = self.coeur.recv(globals.HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        message = self.coeur.recv(message_length).decode('utf-8')
        return message == "pong"