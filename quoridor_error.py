class QuoridorError(Exception):
    """Classe pour encapsuler les erreurs du jeu Quoridor.


    Attributes:
        self.état (dict): self.état du jeu tenu à jour."""   
    def __init__(self, message):
        """Constructeur de la classe QuoridorError
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
        super().__init__(message)

    def etat_courant(self, état):
        """Etat courant
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
        return état
