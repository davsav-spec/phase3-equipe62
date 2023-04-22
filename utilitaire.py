"""Module de fonctions utilitaires pour le jeu jeu Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
"""

import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par `parser.parse_args()`.
                    Cet objet a trois attributs: « idul » représentant l'idul
                    du joueur, « parties » qui est un booléen `True`/`False`
                    et « local » qui est un booléen `True`/`False`.
    """
    parser = argparse.ArgumentParser(description='Quoridor')
    parser.add_argument('idul', type=str, help='IDUL du joueur')
    parser.add_argument('-p', '--parties', metavar='', type=bool,\
    help='Lister les parties existantes')
    return parser.parse_args()

    # Complétez le code ici




def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre rester exactement la même que ce qui est passé en paramètre.
    Args:
        parties (list): Liste des parties
    Returns:
        str: Représentation des parties
    """
    formater_parties = ''
    for i in range(len(parties)):
        date = parties[i]['date']
        j1, j2 = parties[i]['joueurs'][0], parties[i]['joueurs'][1]
        gagnant = parties[i]['gagnant']
        formater_parties += str(i+1) + ' : ' + date + ', ' + j1+ ' vs ' + j2
        if gagnant is not None:
            formater_parties += ', ' + 'gagnant: ' + gagnant + '\n'
        else:
            formater_parties += '\n'
    return formater_parties
