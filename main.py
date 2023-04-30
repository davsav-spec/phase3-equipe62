"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
from api import débuter_partie, jouer_coup, lister_parties
from quoridor import Quoridor
from utilitaire import analyser_commande, formater_les_parties
from quoridorx import QuoridorX
from utilitaire import analyser_commande
import networkx as nx

# Mettre ici votre secret récupéré depuis le site de PAX
SECRET = "688027b2-8022-4e66-beb3-bffb4c0dc2bf"

if __name__ == "__main__":
    args = analyser_commande()
    if args.automatique and args.graphique:
        
        id_partie, état = débuter_partie(args.idul, SECRET)
        while True:
            game = QuoridorX(état['joueurs'], état['murs'])
            game.afficher()

            try:
                type_coup, position = jouer_le_coup()
                id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)

            except(RuntimeError, PermissionError):

            try:
                type_coup = 'D'
                position = list(nx.shortest_path(game.graphe, tuple(game.état['joueurs'][0]['pos']), 'B1'))[1]
                id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
            except(StopIteration):
                game.est_terminée()
                break


    elif args.graphique:
        id_partie, état = débuter_partie(args.idul, SECRET)
        game = QuoridorX(état['joueurs'], état['murs'])
        while True:
            move, position = game.afficher()
            if move == 'D':
                game.déplacer_jeton(1, position)
            elif move == 'MH':
                game.placer_un_mur(1, position, 'horizontal')
            elif move == 'MV':
                game.placer_un_mur(1, position, 'verticale')
            game.état = game.vérification(game.état['joueurs'], game.état['murs'])
            id_partie, game.état = jouer_coup(id_partie, move, position, args.idul, SECRET)
    
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
            print(i)