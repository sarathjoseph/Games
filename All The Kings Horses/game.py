from board import Board, Piece

from player import Player

from algorithms import best_move, free_knights_evaluation, euclidean_distance_evaluation, play

if __name__ == "__main__":

    """
    WK : White Knight
    BK : Black Knight

    """
    p1_tokens = [Piece("WK1", (2, 2), "white", unichr(9822)), Piece("WK2", (3, 3), "white", unichr(9822))]
    p2_tokens = [Piece("BK1", (2, 3), "black", unichr(9816)), Piece("BK2", (3, 2), "black", unichr(9816))]

    p1 = Player(p1_tokens, "PLAYER1")
    p2 = Player(p2_tokens, "PLAYER2")

    pieces = p1_tokens + p2_tokens
    players = [p1, p2]

    b = Board(pieces, 6, players)

    def test_cases(num):

        """

        :param num: TEST CASE NUMBER

        TEST CASES

        1 : DEFAULT ALPHA BETA PRUNING
        2 : ALPHA BETA WITH FREE KNIGHTS FUNCTION EVALUATION
        3 : ALPHA BETA WITH EUCLIDEAN DISTANCE FUNCTION EVALUATION
        4 : A WHOLE GAME (USING KNIGHTS EVALUATION FUNCTION)
        5 : A WHOLE GAME (USING BOTH KNIGHTS EVALUATION AND EUCLIDEAN E FUNCTION)

        """

        print("\n Initial board state \n")
        print(b)
        print("\n")

        if num == 1:

            """ Test Case 1 : DEFAULT ALPHA BETA PRUNING  """

            win_move = best_move(b, p2, False)
            print_move(win_move)

        elif num == 2:

            """ Test Case 2 : ALPHA BETA WITH FREE KNIGHTS FUNCTION EVALUATION  """

            win_move = best_move(b, p2, free_knights_evaluation)
            print_move(win_move)

        elif num == 3:

            """ Test Case 3 : ALPHA BETA WITH EUCLIDEAN DISTANCE FUNCTION EVALUATION  """

            win_move = best_move(b, p2, euclidean_distance_evaluation)
            print(win_move)

        elif num == 4:

            """ Test Case 4 : A WHOLE GAME PLAYED OUT BETWEEN THE TWO PLAYERS WITH EVALUATION FUNCTION OF CHOICE """
            evaluation = dict()

            # Set choice of evaluation functions here

            evaluation["player1"] = free_knights_evaluation
            evaluation["player2"] = free_knights_evaluation

            game = play(b, p2, evaluation)

            for moves in game:
                print(moves)

        elif num == 5:
            """ Test Case 5 : A WHOLE GAME PLAYED OUT BETWEEN THE TWO PLAYERS WITH BOTH EVALUATION FUNCTION """
            evaluation = dict()

            # Set choice of evaluation functions here

            evaluation["player1"] = euclidean_distance_evaluation
            evaluation["player2"] = free_knights_evaluation

            game = play(b, p2, evaluation)

            for moves in game:
                print(moves)

    def print_move(win_move):

        if win_move:

            print("Next best move \n ")
            print(win_move)

        else:

            print("Player will lose")

    # EXECUTION OF TEST CASES - SELECT ONE OF THE TEST CASES

    test_cases(4)










