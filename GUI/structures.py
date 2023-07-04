__author__ = "reza0310"

import commandes
import utils
import cypher
import connexions
import globals


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
                          "credits": commandes.credits}

    def send(self, commande):
        if commande == "quit":
            framework.stop()
        commande = commande.split(" ")
        if commande[0] not in self.commandes.keys():
            raise Exception("Command not found !")
        else:
            kwargs = {}
            i = 1
            while i < len(commande):
                if commande[i][0:2] == "--":
                    if i == len(commande)-1 or commande[i+1][0:2] == "--":
                        kwargs[commande[i][2:]] = True
                    else:
                        kwargs[commande[i][2:]] = commande[i+1]
                        commande.pop(i+1)
                    commande.pop(i)
                    i -= 1
                i += 1
            try:
                return self.commandes[commande[0]](*commande[1:], **kwargs)
            except Exception as e:
                print(e)
                raise Exception("Bad arguments !")