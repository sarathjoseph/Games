__author__ = 'joseph'


from board import Piece
import copy


class Player():
    def __init__(self, pieces, name):

        if len(pieces) > 0:
            self.color = pieces[0].color
            self.piece_unicode = pieces[0].image
        self.tokens = []
        self.name = name

        for piece in pieces:
            self.tokens.append(piece.name)


def get_valid_moves(board, player):
    m = {}
    n = 0

    for token in player.tokens:
        moves = []
        i, j = board.game_state[token]

        # Knight move validation
        moves.append([(i - 2, j - 1), (i - 1, j - 2), (i + 1, j - 2), (i - 2, j + 1)])
        moves = [(a, b) for (a, b) in moves[0] if
                 all([a > -1 and b > -1, a < board.size and b < board.size, (a, b) not in board.get_occupied()])]

        m[token] = moves
        n += len(moves)

    return m, n


def get_next_board_positions(board, player):
    moves, n = get_valid_moves(board, player)

    boards = [copy.deepcopy(board) for _ in range(0, n)]
    i = 0

    for m in moves:
        for position in moves[m]:
            boards[i].update_board([Piece(m, position, player.color, player.piece_unicode)])
            i += 1

    return boards