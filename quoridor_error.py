class QuoridorError(Exception):   
    def __init__(self, message):
        super().__init__(message)

    def etat_courant(self, état):
        return état
