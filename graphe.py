"""Module de construction d'un graphe

Functions:
    * construire_graphe - Construire un graphe de la grille.
"""

import networkx as nx
import matplotlib.pyplot as plt

def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    """Construire un graphe de la grille.

    Crée le graphe des déplacements admissibles pour les joueurs.
    Vous n'avez pas à modifier cette fonction.

    Args:
        joueurs (List): une liste des positions [x,y] des joueurs.
        murs_horizontaux (List): une liste des positions [x,y] des murs horizontaux.
        murs_verticaux (List): une liste des positions [x,y] des murs verticaux.

    Returns:
        DiGraph: le graphe bidirectionnel (en networkX) des déplacements admissibles.
    """
    graphe = nx.DiGraph()

    # pour chaque colonne du damier
    for x in range(1, 10):
        # pour chaque ligne du damier
        for y in range(1, 10):
            # ajouter les arcs de tous les déplacements possibles pour cette tuile
            if x > 1:
                graphe.add_edge((x, y), (x - 1, y))
            if x < 9:
                graphe.add_edge((x, y), (x + 1, y))
            if y > 1:
                graphe.add_edge((x, y), (x, y - 1))
            if y < 9:
                graphe.add_edge((x, y), (x, y + 1))

    # retirer tous les arcs qui croisent les murs horizontaux
    for x, y in murs_horizontaux:
        graphe.remove_edge((x, y - 1), (x, y))
        graphe.remove_edge((x, y), (x, y - 1))
        graphe.remove_edge((x + 1, y - 1), (x + 1, y))
        graphe.remove_edge((x + 1, y), (x + 1, y - 1))

    # retirer tous les arcs qui croisent les murs verticaux
    for x, y in murs_verticaux:
        graphe.remove_edge((x - 1, y), (x, y))
        graphe.remove_edge((x, y), (x - 1, y))
        graphe.remove_edge((x - 1, y + 1), (x, y + 1))
        graphe.remove_edge((x, y + 1), (x - 1, y + 1))

    # s'assurer que les positions des joueurs sont bien des tuples (et non des listes)
    j1, j2 = tuple(joueurs[0]), tuple(joueurs[1])

    # traiter le cas des joueurs adjacents
    if j2 in graphe.successors(j1) or j1 in graphe.successors(j2):
        # retirer les liens entre les joueurs
        graphe.remove_edge(j1, j2)
        graphe.remove_edge(j2, j1)

        def ajouter_lien_sauteur(noeud, voisin):
            """
            :param noeud: noeud de départ du lien.
            :param voisin: voisin par dessus lequel il faut sauter.
            """
            saut = 2 * voisin[0] - noeud[0], 2 * voisin[1] - noeud[1]

            if saut in graphe.successors(voisin):
                # ajouter le saut en ligne droite
                graphe.add_edge(noeud, saut)

            else:
                # ajouter les sauts en diagonale
                for saut in graphe.successors(voisin):
                    graphe.add_edge(noeud, saut)

        ajouter_lien_sauteur(j1, j2)
        ajouter_lien_sauteur(j2, j1)

    # ajouter les destinations finales des joueurs
    for x in range(1, 10):
        graphe.add_edge((x, 9), "B1")
        graphe.add_edge((x, 1), "B2")

    return graphe


état = {
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": (5, 6)},
        {"nom": "automate", "murs": 3, "pos": (5, 7)}
    ],
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
        "verticaux": [[6, 2], [4, 4], [2, 5], [7, 5], [7, 7]]
    }
}

graphe = construire_graphe(
    [joueur['pos'] for joueur in état['joueurs']],
    état['murs']['horizontaux'],
    état['murs']['verticaux']
)


positions = {'B1': (5, 10), 'B2': (5, 0)}
colors = {
    'B1': 'red', 'B2': 'green',
    tuple(état['joueurs'][0]['pos']): 'red',
    tuple(état['joueurs'][1]['pos']): 'green',
}
sizes = {
    tuple(état['joueurs'][0]['pos']): 300,
    tuple(état['joueurs'][1]['pos']): 300
}

nx.draw(
    graphe,
    pos={node: positions.get(node, node) for node in graphe},
    node_size=[sizes.get(node, 100) for node in graphe],
    node_color=[colors.get(node, 'gray') for node in graphe],
)
plt.show()


print(list(graphe.successors((5,6))))
print(nx.has_path(graphe, (5,6), 'B1'))
print(nx.shortest_path(graphe, (5,6), 'B1'))