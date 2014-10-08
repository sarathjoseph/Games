

<b>REPRESENTATION <b>

The representation uses the following classes

Board
Player
Piece
	
A Piece class is instantiated with the initial position , the name ,color and unicode representation of the piece 

A Player class is instantiated with a name and passed the tokens (pieces)

A Board class is instantiated with the players, pieces and size of the board


<b>BOARD CLASS</b>
               
The Board contains two key methods

update_board 
get_occupied

The get_occupied method is used to check the board state for squares that are occupied
The update_board method is used to change the board state and shuffle around pieces

The class also contains the following key instance variables

size
players
game_state ( holds location of the four knights)
state ( Its a 2-D array  containing the entire board representation.)





Example Initialization

a = [Piece("WK1", (2, 2), "white", unichr(9822)), Piece("WK2", (3, 3), "white", unichr(9822))]

p1 = Player(a,"Player1")

b = Board(pieces, 6, players)


<b>SUCCESSOR FUNCTIONS</b>

There are two functions that do the job of successor functions for this game

get_next_board_positions
get_valid_moves

get_valid_moves takes in a board state and a player and returns the set of valid moves

get_next_board_positions 

calls get_valid_moves to obtain valid states
makes boards for all the valid states and returns them	

<b>BEST_MOVE </b>

The best_move takes in three params - the player to move, board state and the evaluation
function to use. The function returns a board with the best move

The e_function param (captures the evaluation function to use) can take three values

TRUE (Uses the default Alpha beta pruning )
euclidean_distance_evaluation 
free_knights_evaluation

The euclidean_distance_evaluation and free_knights_evaluation are passed in as callbacks.

Example Usage

best_move(b, p2, free_knights_evaluation)
best_move(b, p1, euclidean_distance_evaluation)

where p1 and p2 are PLAYER 1 and PLAYER 2 respectively
PRUNING 

To prune the game search two evaluation functions were used 

euclidean_distance_evaluation 
free_knights_evaluation


<b>Free Knights Evaluation</b>

The rationale behind choosing this evaluation is that a terminal state that ends in more mobility for horses should be given higher value that the ones with lesser. 

Example  For a max_player,  a win with both horses capable of making four moves each should be preferred over a win state where both the horses are only capable of making less than 8 moves together.

For every mobile horse in a terminal state 2 points are awarded or deducted based on whether it is a win or a loss


Implementation

Whenever a terminal state is encountered, the requisite evaluation function is called passing in the opponent player object. The opponents position is extracted and the points to be awarded or deducted are evaluated by multiplying the sum of legal moves for both knights by 2 or -2. 

Euclidean Distance Evaluation

The Euclidean Distance Evaluation function computes the distance between the pair of horses in a terminal node. Higher difference in distance means in essence more mobility and more chances of winning or losing. More mobility because larger the distance between two pieces, the lesser the chances of impeding each other’s moves.

Implementation

The location of both pair horses are extracted from the board state and the sum of the euclidean distance between each of pair of horses of opposite horses is computed. 
The floor function is called on the sum and is added to the win state value of +1 or deducted from the loss state value of -1


<b>OUTPUT</b>

complete game played between players with evaluation choice . 

 game = play(b, p2, evaluation) - Player 2 starts the game and 

NOTE : Intermediate states are not shown here although they are printed in original output

Initial board state                   

■  ■  ■  ■  ■  ■  

■  ■  ■  ■  ■  ■  

■  ■  ♞  ♘  ■  ■  

■  ■  ♘  ♞  ■  ■  

■  ■  ■  ■  ■  ■  
 
■  ■  ■  ■  ■  ■  



End State 


♘  ■  ■  ■  ■  ■  

♞  ♞  ■  ■  ■  ■  

♘  ■  ■  ■  ■  ■  

■  ■  ■  ■  ■  ■  

■  ■  ■  ■  ■  ■  

■  ■  ■  ■  ■  ■  


(Figure 1.1)

<b>TEST CASES</b>

        1 : DEFAULT ALPHA BETA PRUNING
        2 : ALPHA BETA WITH FREE KNIGHTS FUNCTION EVALUATION
        3 : ALPHA BETA WITH EUCLIDEAN DISTANCE FUNCTION EVALUATION
        4 : A WHOLE GAME (USING KNIGHTS EVALUATION FUNCTION)
        5 : A WHOLE GAME (USING BOTH EVALUATION FUNCTIONS)

Note : Run game.py  and run the required test case as  test_cases(number). 
eg. test_cases(4)


<b>RESULTS</b>

A brute force approach (minimax) takes approximately one minute for the following initial state to compute the best move

Initial board state                   

■  ■  ■  ■  ■  ■  

■  ■  ■  ■  ■  ■  

■  ■  ♞  ♘  ■  ■  

■  ■  ♘  ♞  ■  ■  

■  ■  ■  ■  ■  ■  
 
■  ■  ■  ■  ■  ■  

(Figure 1.2)

Alpha beta pruning takes less than a second for the same initial input configuration. 





<b>OBSERVATIONS</b>

A board size beyond dimensions 10 * 10 takes a very large time to complete. 

For the initial configuration (Fig 1.2) , Black Wins with whether or not it starts first irrespective of the evaluation functions used. 



