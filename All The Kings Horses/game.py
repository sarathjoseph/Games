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

    def test_cases(test):

        """

        :param num: TEST CASE NUMBER

        TEST CASES

        1 : DEFAULT ALPHA BETA PRUNING


       NOTE : More Test cases for depth limited search to be added later Depth limited search to be added later

        """

        print("\n Initial board state \n")
        print(b)
        print("\n")

        if test == 1:

            """ Test Case 1 : DEFAULT ALPHA BETA PRUNING  """

            win_move = best_move(b, p2, False)
            print_move(win_move)


    def print_move(win_move):

        if win_move:

            print("Next best move \n ")
            print(win_move)

        else:

            print("Player will lose")

    # EXECUTION OF TEST CASES - SELECT ONE OF THE TEST CASES

    test_cases(1)










