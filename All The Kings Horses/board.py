
box_unicode = u"\u25A0"


class Board():

    def __init__(self, pieces, size, players):

        self.empty_squares = box_unicode
        self.state = [[self.empty_squares] * size for _ in range(0, size)]
        self.size = size
        self.game_state = {}
        self.players = players
        self.update_board(pieces)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def get_occupied(self):

        occupied = []

        for i in range(0, self.size):

            for j in range(0, self.size):

                piece = self.state[i][j]

                if piece is not self.empty_squares:
                    occupied.append((i, j))

        return occupied

    def update_board(self, pieces):

        for piece in pieces:

            if piece.name in self.game_state:
                x, y = self.game_state[piece.name]
                self.state[x][y] = self.empty_squares

            i, j = piece.position
            self.state[i][j] = piece
            self.game_state[piece.name] = (i, j)

    def __unicode__(self):

        string = ""

        for i in range(0, self.size):

            for j in range(0, self.size):

                piece = self.state[i][j]

                if piece is not self.empty_squares:

                    icon = piece.image
                    string += icon + "  "
                else:
                    string += self.empty_squares + "  "

            string += "\n\n"

        return string


class Piece():

    def __init__(self, name, position, color, image):
        self.name = name
        self.color = color
        self.position = position
        self.image = image

    def __str__(self):
        return self.image
