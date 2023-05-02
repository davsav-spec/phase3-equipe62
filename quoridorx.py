from quoridor import Quoridor
import turtle
class QuoridorX(Quoridor):
    def __init__(self,joueurs, murs):
        super().__init__(joueurs, murs)
        self.__turtle = turtle.Turtle()
        self.__turtle.speed(0)
        self.__turtle.hideturtle()
        self.__turtle.penup()
        self.__draw_board()
        self.afficher()

    def afficher(self):
        self.__draw_pawns()
        turtle.mainloop()

    def __draw_board(self):
        self.__turtle.goto(-180, 180)
        self.__turtle.pendown()
        self.__turtle.goto(180, 180)
        self.__turtle.goto(180, -180)
        self.__turtle.goto(-180, -180)
        self.__turtle.goto(-180, 180)
        self.__draw_lines()

    def __draw_lines(self):
        for i in range(8):
            self.__turtle.penup()
            self.__turtle.goto(-180, 140 - 40 * i)
            self.__turtle.pendown()
            self.__turtle.goto(180, 140 - 40 * i)

        self.__turtle.penup()
        self.__turtle.goto(-140, 180)

        for i in range(8):
            self.__turtle.penup()
            self.__turtle.goto(-140 + 40 * i, 180)
            self.__turtle.pendown()
            self.__turtle.goto(-140 + 40 * i, -180)

    def __draw_pawns(self):
        for i in range(2):
            pawn = self.obtenir_positions_pions()[i]
            self.__turtle.penup()
            self.__turtle.goto(-160 + 320 * pawn[0], -160 + 320 * pawn[1])
            self.__turtle.dot(30, self.obtenir_joueurs()[i+1].couleur)

        for i in range(2):
            walls = self.obtenir_positions_murs(i+1)
            for wall in walls:
                self.__turtle.penup()
                self.__turtle.goto(-170 + 40 * wall[0], -170 + 40 * wall[1])
                self.__turtle.pendown()
                self.__turtle.setheading(0)
                self.__turtle.forward(20)
                self.__turtle.right(90)
                self.__turtle.forward(40)
                self.__turtle.right(90)
                self.__turtle.forward(20)
                self.__turtle.right(90)
                self.__turtle.forward(40)

                self.__turtle.penup()
                self.__turtle.goto(-180 + 40 * wall[0], -180 + 40 * wall[1])
                self.__turtle.pendown()
                self.__turtle.setheading(0)
                self.__turtle.forward(40)
                self.__turtle.right(90)
                self.__turtle.forward(20)
                self.__turtle.right(90)
                self.__turtle.forward(40)
                self.__turtle.right(90)
                self.__turtle.forward(20)

#x = QuoridorX(joueurs, murs)
#print(x)
