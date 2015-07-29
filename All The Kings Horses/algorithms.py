__author__ = 'joseph'

from player import get_next_board_positions
import math


def min_max(board, player, depth, max_player):
    if depth == 0:
        first_level = True
    else:
        first_level = False

    opponent = [p for p in board.players if not p.name == player.name][0]

    if max_player:
        best_val = -10
        boards = get_next_board_positions(board, player)

        # if no boards are returned then its a loss
        if not boards:
            return -1

        for b in boards:
            depth += 1
            val = min_max(b, opponent, depth, False)
            best_val = max(best_val, val)

            if first_level and best_val == 1:
                return b

        return best_val

    else:
        best_val = 10

        boards = get_next_board_positions(board, player)
        if not boards:
            return 1

        for b in boards:
            depth += 1
            val = min_max(b, opponent, depth, True)
            best_val = min(best_val, val)
        return best_val


def alpha_beta(board, alpha, beta, player, depth, max_player):
    if depth == 0:
        first_level = True
    else:
        first_level = False

    opponent = [p for p in board.players if not p.name == player.name][0]

    if max_player:

        boards = get_next_board_positions(board, player)

        # if no boards are returned then its a loss
        if not boards:
            return -1

        for b in boards:
            depth += 1
            alpha = max(alpha, alpha_beta(b, alpha, beta, opponent, depth, False))
            if beta <= alpha:
                break
            if first_level and alpha == 1:
                return b
        return alpha

    else:
        boards = get_next_board_positions(board, player)

        if not boards:
            return 1

        for b in boards:
            depth += 1
            beta = min(beta, alpha_beta(b, alpha, beta, opponent, depth, True))
            if beta <= alpha:
                break
        return beta

'''

""" THIS NEEDS TO BE MODIFIED TO SUPPORT DEPTH LIMITED SEARCH """



def free_knights_evaluation(board, player, max_player):
    """

    Returns the points gained or lost by evaluating the positioning of knights in a terminal node. A mobile knight in a
    terminal node has 2 points associated with it for every valid move.

    """

    points = 0

    for token in player.tokens:
        moves = []
        i, j = board.game_state[token]
        moves.append([(i - 2, j - 1), (i - 1, j - 2), (i + 1, j - 2), (i - 2, j + 1)])
        moves = [(a, b) for (a, b) in moves[0] if
                 all([a > -1 and b > -1, a < board.size and b < board.size, (a, b) not in board.get_occupied()])]

        if max_player:
            points += len(moves) * 2
        else:
            points -= len(moves) * 2

    return points


def euclidean_distance_evaluation(board, player, max_player):
    """

     Computes Euclidean distance between the knights . The return value corresponds to the distance between opposing knights

    """

    points = 0

    opponent = [p for p in board.players if not p.name == player.name][0]

    player_position, opponent_position = [], []

    for token in player.tokens:
        i, j = board.game_state[token]
        player_position.append((i, j))

    for token in opponent.tokens:
        i, j = board.game_state[token]
        opponent_position.append((i, j))

    d1 = math.hypot(opponent_position[0][0] - player_position[0][0], opponent_position[0][1] - player_position[0][1])
    d2 = math.hypot(opponent_position[1][0] - player_position[1][0], opponent_position[1][1] - player_position[1][1])

    if max_player:
        # verify this
        points += int(d1 + d2)
    else:
        points -= int(d1 + d2)
    return points


def alpha_beta_evaluation(board, alpha, beta, player, depth, max_player, e_function):
    """
    :param max_player: Boolean value indicating whether max player or not
    :param e_function: The evaluation function passed as argument to best_move

    """
    if depth == 0:
        first_level = True
        board_store = {}
    else:
        first_level = False

    opponent = [p for p in board.players if not p.name == player.name][0]

    if max_player:

        boards = get_next_board_positions(board, player)

        if not boards:
            if first_level:
                return []
            return -1 + e_function(board, opponent, False)

        for b in boards:
            depth += 1
            alpha = max(alpha, alpha_beta_evaluation(b, alpha, beta, opponent, depth, False, e_function))
            if beta <= alpha:
                break
            if first_level:

                board_store[alpha] = b

        if first_level:
            index = list(reversed(sorted(board_store.keys())))[0]
            return board_store[index]
        return alpha

    else:
        boards = get_next_board_positions(board, player)

        if not boards:
            return 1 + e_function(board, opponent, True)

        for b in boards:
            depth += 1
            beta = min(beta, alpha_beta_evaluation(b, alpha, beta, opponent, depth, True, e_function))
            if beta <= alpha:
                break
        return beta

'''

def best_move(board, player, e_function):
    # set the algorithm to use for default mode (minmax or alpha-beta)
    algorithm = alpha_beta

    if e_function:
        return alpha_beta_evaluation(board, -float("inf"), float("inf"), player, 0, True, e_function)

    elif algorithm.__name__ == "alpha_beta":

        return algorithm(board, -10, 10, player, 0, True)

    elif algorithm.__name__ == "min_max":
        return algorithm(board, player, 0, True)


def play(board, player1, evaluation):
    """

    :param board:   The initial board representation
    :param player1: The Starting player
    :param evaluation: A dictionary containing the evaluation functions used by the 2 players
    :return: returns the  complete game having board positions from start to end
    """

    game = []
    end = False
    move = 1
    player2 = [p for p in board.players if not p.name == player1.name][0]

    while not end:

        if not move % 2 == 0:
            board = best_move(board, player1, evaluation["player1"])

            if not board:
                return game
            else:
                move += 1

                game.append(board)
        else:
            board = best_move(board, player2, evaluation["player2"])

            if not board:

                return game
            else:
                move += 1
                game.append(board)


