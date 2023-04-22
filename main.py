"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
from api import débuter_partie, jouer_coup, lister_parties
from quoridor import Quoridor
from utilitaire import analyser_commande, formater_les_parties

# Mettre ici votre secret récupéré depuis le site de PAX
SECRET = "688027b2-8022-4e66-beb3-bffb4c0dc2bf"

if __name__ == "__main__":
    args = analyser_commande()
    if args.parties:
        parties = lister_parties(args.idul, SECRET)
        print(formater_les_parties(parties))
        #print(formater_les_parties(parties))
    else:
        id_partie, état = débuter_partie(args.idul, SECRET)
        while True:
            # Afficher la partie
            print(str(état))
            # Demander au joueur de choisir son prochain coup
            type_coup, position = Quoridor.récupérer_le_coup()
            # Envoyez le coup au serveur
            id_partie, état = jouer_coup(
                id_partie,
                type_coup,
                position,
                args.idul,
                SECRET,
            )