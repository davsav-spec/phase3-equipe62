"""Module de la classe Quoridor
Classes: Quoridor - Classe pour encapsuler le jeu Quoridor."""

from copy import deepcopy
from quoridor_error import QuoridorError
from graphe import construire_graphe
import networkx as nx
import math

class Quoridor:
    """Classe pour encapsuler le jeu Quoridor.

    Vous ne devez pas créer d'autre attributs pour votre classe.

    Attributes:
        self.état (dict): self.état du jeu tenu à jour."""
    def __init__(self, joueurs, murs=None):
        """Constructeur de la classe Quoridor.
        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.
        Appel la méthode `vérification` pour valider les données et assigne
        ce qu'elle retourne à l'attribut `self.état`.
        Cette méthode ne devrait pas être modifiée.
        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux."""
        self.état = deepcopy(self.vérification(joueurs, murs))

    def vérification(self, joueurs, murs):
        """Vérification d'initialisation d'une instance de la classe Quoridor.
        Valide les données arguments de construction de l'instance et retourne
        l'self.état si valide.
        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        Returns:
            Dict: Une copie de l'self.état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de list [x, y] uniquement.
        Raises:
            QuoridorError: L'argument 'joueurs' n'est pas itérable. X
            QuoridorError: L'itérable de joueurs en contient un nombre différent de deux. X
            QuoridorError: Le nombre de murs qu'un joueur peut placer est plus grand que 10,
                            ou négatif. X
            QuoridorError: La position d'un joueur est invalide. X
            QuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent. X
            QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20. X
            QuoridorError: La position d'un mur est invalide. X"""
        if not isinstance(joueurs, (list, tuple)):
            raise QuoridorError("L'argument 'joueurs' n'est pas itérable.")
        if len(joueurs) != 2:
            raise QuoridorError("L'itérable de joueurs en contient un nombre différent de deux.")
        #nb murs joueur 1
        if joueurs[0]['murs'] > 10 or joueurs[0]['murs'] < 0:
            raise QuoridorError("Le nombre de murs qu'un joueur peut placer est\
                                plus grand que 10, ou négatif.")
        #nb murs joueur 2
        if joueurs[1]['murs'] > 10 or joueurs[1]['murs'] < 0:
            raise QuoridorError("Le nombre de murs qu'un joueur peut placer est\
                                 plus grand que 10, ou négatif.")

        #position invalide
        for i in joueurs[0]['pos']:
            if i < 1 or i > 9:
                raise QuoridorError("La position d'un joueur est invalide.")
        for i in joueurs[1]['pos']:
            if i < 1 or i > 9:
                raise QuoridorError("La position d'un joueur est invalide.")

        if murs is None:
            murs = {'horizontaux': [], 'verticaux': []}
        else:
            if not isinstance(murs, dict):
                raise QuoridorError("L'argument 'murs' n'est pas un\
                                     dictionnaire lorsque présent.")

        if (joueurs[0]['murs'] + joueurs[1]['murs'] + len(murs["horizontaux"]) + len(murs["verticaux"])) != 20:
            raise QuoridorError("Le total des murs placés et plaçables n'est pas égal à 20")

        #mur invalide
        for i in murs["horizontaux"]:
            if (i[0] > 8 or i[0] < 1) or (i[1] < 2 or i[1] > 9):
                raise QuoridorError("La position d'un mur est invalide.")
        for i in murs["verticaux"]:
            if (i[0] > 9 or i[0] < 2) or (i[1] < 1 or i[1] > 8):
                raise QuoridorError("La position d'un mur est invalide.")

        #return deepcopy(joueurs, murs)
        #return deepcopy(self.état(joueurs, murs))
        return {'joueurs': joueurs, 'murs': murs}



    def formater_légende(self):
        """Formater la représentation graphique de la légende.

        Returns:
            str: Chaîne de caractères représentant la légende."""
        légende = ''
        m1 = self.état['joueurs'][0]['murs']*'|'
        m2 = self.état['joueurs'][1]['murs']*'|'
        j1 = self.état['joueurs'][0]["nom"]
        j2 = self.état['joueurs'][1]['nom']
        if len(self.état['joueurs'][0]["nom"]) < len(self.état['joueurs'][1]["nom"]):
            x = (len(self.état['joueurs'][1]["nom"]) - len(self.état['joueurs'][0]["nom"]))*' ' + ' '
            légende += 'Légende:' + '\n'
            légende += f'   1={j1},{x}murs={m1}\n'
            légende += f'   2={j2}, murs={m2}\n'
        elif len(self.état['joueurs'][0]["nom"]) > len(self.état['joueurs'][1]["nom"]):
            x = (len(self.état['joueurs'][0]["nom"]) - len(self.état['joueurs'][1]["nom"]))*' ' + ' '
            légende += 'Légende:' + '\n'
            légende += f'   1={j1}, murs={m1}\n'
            légende += f'   2={j2},{x}murs={m2}\n'
        else:
            légende += 'Légende:' + '\n'
            légende += f'   1={j1}, murs={m1}\n'
            légende += f'   2={j2}, murs={m2}\n'
        return légende


    def formater_damier(self):
        """Formater la représentation graphique du damier.

        Returns:
            str: Chaîne de caractères représentant le damier."""
        a = '   ' + '-'*35 + '\n'
        b = ' ' + '.   '*8 + '. '
        for x in range(9, 0, -1):
            if x > 1:
                a += f'{x} |{b}|\n' + ('  |' + 35*' ' + '|' '\n')
                grille = a + '-'*2 + '|' + 35*'-'
            else:
                a += f'{x} |{b}|\n'
                grille = a + '-'*2 + '|' + 35*'-' + '\n' + '  | '

        for y in range(1, 10):
            if y == 9:
                grille += f'{y}'
            else:
                grille += f'{y}   '


        murs_hori_liste = self.état['murs']['horizontaux']
        murs_verti_liste = self.état['murs']['verticaux']

        liste_ligne = grille.split('\n')
        #placer les tirets
        for mur_h in murs_hori_liste:
            coord_verti_mur = mur_h[1]
            coord_verti_mur_inver = 10 - coord_verti_mur
            indice_ligne = 2 * coord_verti_mur_inver
        #bonne ligne dans la liste
            coord_hori_mur = mur_h[0]
            i_colonne_start = 3 + (coord_hori_mur - 1) * 4
            i_colonne_fin = i_colonne_start + 7
        #spot à remplacer + reste de la ligne
            nouvelle_ligne = liste_ligne[indice_ligne][0:i_colonne_start]\
            + '-------' + liste_ligne[indice_ligne][i_colonne_fin:]
        #remplacer l'ancienne ligne
            liste_ligne[indice_ligne] = nouvelle_ligne

        for mur_v in murs_verti_liste:
        #bonne ligne à modifier (indice)
            coord_verti_mur = mur_v[1]
            coord_verti_mur_inver = 2*(9 - coord_verti_mur) - 1
            i_ligne_modif = [coord_verti_mur_inver,
            coord_verti_mur_inver+1, coord_verti_mur_inver+2]
        #modifier la ligne avec bonnne colonne
            coord_hori_mur = mur_v[0]
            i_colonne = 6 + (coord_hori_mur - 2) * 4

            for ligne_indice in i_ligne_modif:
                nouvelle_ligne = liste_ligne[ligne_indice][0:i_colonne]\
                + "|" + liste_ligne[ligne_indice][i_colonne+1:]
                liste_ligne[ligne_indice] = nouvelle_ligne

        p1 = self.état['joueurs'][0]["pos"]
        p2 = self.état['joueurs'][1]['pos']
        #placer pion 1
        coor_v_p1 = p1[1]
        coor_v_p1_inv = -(2*(-9 + coor_v_p1)-1)
        i_bonne_ligne = coor_v_p1_inv
        coor_h_p1 = p1[0]
        i_p_start = (coor_h_p1) *4
        i_p_fin = i_p_start + 1
        nouvelle_ligne = liste_ligne[i_bonne_ligne][0:i_p_start]\
        + '1' + liste_ligne[i_bonne_ligne][i_p_fin:]
        liste_ligne[i_bonne_ligne] = nouvelle_ligne
        #placer pion 2
        coor_v_p2 = p2[1]
        coor_v_p2_inv = -(2*(-9 + coor_v_p2)-1)
        i_bonne_ligne = coor_v_p2_inv
        coor_h_p2 = p2[0]
        i_p_start = (coor_h_p2) *4
        i_p_fin = i_p_start + 1
        nouvelle_ligne = liste_ligne[i_bonne_ligne][0:i_p_start]\
        + '2' + liste_ligne[i_bonne_ligne][i_p_fin:]
        liste_ligne[i_bonne_ligne] = nouvelle_ligne

        #réaffiche la ligne
        nouvelle_grille = ''
        for i in liste_ligne:
            nouvelle_grille += i + '\n'
        return nouvelle_grille


    def __str__(self):
        """Représentation en art ascii de l'état actuel de la partie.

        Cette représentation est la même que celle du projet précédent.

        Returns:
            str: La chaîne de caractères de la représentation."""
        return self.formater_légende() + self.formater_damier()


    def état_courant(self):
        """Produire l'état actuel du jeu.

        Cette méthode ne doit pas être modifiée.

        Returns:
            Dict: Une copie de l'self.état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de liste [x, y] uniquement.
        """
        return deepcopy(self.état)


    def est_terminée(self):
        """Déterminer si la partie est terminée.
        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        if self.état['joueurs'][0]['pos'][1] == 9:
            return self.état_courant['joueurs'][0]['nom']
        elif self.état['joueurs'][1]['pos'][1] == 1:
            return self.état['joueurs'][1]['nom']
        else:
            return False


    def récupérer_le_coup(self, joueur):
        """Récupérer le coup

        Notez que seul 2 questions devrait être posée à l'utilisateur.

        Notez aussi que cette méthode ne devrait pas modifier l'self.état du jeu.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Le type de coup est invalide.
            QuoridorError: La position est invalide (en dehors du damier).

        Returns:
            tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y]."""
        if joueur not in [1, 2]:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        coups_valides = ["D", "MH", "MV"]
        le_type_de_coup = input("Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'): {}: ".format(joueur))
        if le_type_de_coup not in coups_valides:
            raise QuoridorError("Le type de coup est invalide.")
        try:
            position = list(map(int, input("Donnez la position où appliquer ce coup (x,y): {}: ".format(joueur)).split(',')))
        except:
            raise QuoridorError("La position est invalide (en dehors du damier).")
        if not(1 <= position[0] <= 9) or not(1 <= position[1] <= 9):
            raise QuoridorError("La position est invalide (en dehors du damier).")
        return (le_type_de_coup, position)
        

    def déplacer_jeton(self, joueur, position):
        """Déplace un jeton.
        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.
        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (List[int, int]): La liste [x, y] de la position du jeton (1<=x<=9 et 1<=y<=9).
        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La position est invalide (en dehors du damier).
            QuoridorError: La position est invalide pour l'self.état actuel du jeu."""
        if joueur not in [1, 2]:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        if not (1 <= position[0] <= 9) or not (1 <= position[1] <= 9):
            raise QuoridorError("La position est invalide (en dehors du damier).")
        if position == self.état["joueurs"][0]["pos"] and self.état["joueurs"][1]["pos"]:
            raise QuoridorError("La position est invalide pour l'état actuel du jeu.")
        self.état["joueurs"][joueur-1]["pos"] = position


    def placer_un_mur(self, joueur, position, orientation):
        """Placer un mur.

        Pour le joueur spécifié, placer un mur à la position spécifiée.

        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (List[int, int]): la liste [x, y] de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Un mur occupe déjà cette position.
            QuoridorError: La position est invalide pour cette orientation.
            QuoridorError: Le joueur a déjà placé tous ses murs.       """
        if joueur not in [1, 2]:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        if orientation == "horizontal":
            murs1 = self.état["murs"]["horizontaux"]
            if position[0] < 1 or position[0] > 8 or position[1] < 2 or position[1] > 9:
                raise QuoridorError("La position est invalide pour cette orientation.")
            if [position[0] - 1, position[1]] in murs1 or [position[0], position[1]] in murs1:
                raise QuoridorError("Un mur occupe déjà cette position.")
        else:
            murs2 = self.état["murs"]["verticaux"]
            if position[0] < 2 or position[0] > 9 or position[1] < 1 or position[1] > 8:
                raise QuoridorError("La position est invalide pour cette orientation.")
            if [position[0], position[1] - 1] in murs2 or [position[0], position[1]] in murs2:
                raise QuoridorError("Un mur occupe déjà cette position.")

        if self.état['joueurs'][joueur-1]['murs'] == 0:
        #if len(self.murs[joueur-1]) == 10:
            raise QuoridorError("Le joueur a déjà placé tous ses murs.")

        #placer les murs
        if orientation == "horizontal":
            self.état["murs"]["horizontaux"].append(position)
            self.état["murs"]["horizontaux"].sort()
        else:
            self.état["murs"]["verticaux"].append(position)
            self.état["murs"]["verticaux"].sort()

        #murs restants
        self.état['joueurs'][joueur-1]['murs'] -= 1


    def jouer_le_coup(self, joueur):
        """Jouer un coup automatique pour un joueur.
        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'self.état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.
        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La partie est déjà terminée.
        Returns:
            Tuple[str, List[int, int]]: Un tuple composé du type et de la position du coup joué."""
        if joueur not in [1, 2]:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        if self.est_terminée():
            raise QuoridorError("La partie est déjà terminée.")
        
        # Construire le graphe
        graphe = construire_graphe([self.état["joueurs"][0]["pos"], self.état["joueurs"][1]["pos"]], self.état["murs"]["horizontaux"], self.état["murs"]["verticaux"])
        
        # Trouver le plus court chemin pour le joueur et son adversaire
        dest_joueur = "B" + str(joueur)
        dest_adversaire = "B" + str(3 - joueur)
        chemin_joueur = nx.shortest_path(graphe, tuple(self.état["joueurs"][joueur - 1]["pos"]), dest_joueur)
        chemin_adversaire = nx.shortest_path(graphe, tuple(self.état["joueurs"][2 - joueur]["pos"]), dest_adversaire)
        
        # Si le chemin de l'adversaire est plus court, placer un mur pour lui barrer le chemin
        if len(chemin_adversaire) < len(chemin_joueur):
            for i in range(len(chemin_adversaire) - 1):
                pos1 = chemin_adversaire[i]
                pos2 = chemin_adversaire[i + 1]
                if pos1[0] == pos2[0]:
                    orientation = "horizontal"
                    position = (pos1[0], min(pos1[1], pos2[1]))
                else:
                    orientation = "vertical"
                    position = (min(pos1[0], pos2[0]), pos1[1])
                try:
                    self.placer_un_mur(joueur, position, orientation)
                    return ('MH' if orientation == 'horizontal' else 'MV', position)
                except QuoridorError:
                    continue
        
        # Sinon, déplacer le jeton du joueur
        self.déplacer_jeton(joueur, [chemin_joueur[1][0], chemin_joueur[1][1]])
        return ('D', [chemin_joueur[1][0], chemin_joueur[1][1]])