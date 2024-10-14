#!/usr/bin/env python͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
import traceback
from isolation import Board, game_as_text
from test_players import RandomPlayer, HumanPlayer, Player
import platform

if platform.system() != 'Windows':
    import resource

from time import time, sleep

def correctOpenEvalFn(yourOpenEvalFn):
    print()
    try:
        sample_board = Board(RandomPlayer(), RandomPlayer())
        # setting up the board as though we've been playing͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
        board_state = [
            [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
            [' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', 'K2'],
            [' ', ' ', 'X', 'X', ' ', ' ', 'X', ' ', 'X'],
            ['X', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' '],
            [' ', ' ', 'K1', ' ', ' ', ' ', 'X', 'X', ' '],
            [' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X', 'X'],
            [' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X'],
            [' ', ' ', ' ', 'X', 'X', ' ', 'X', 'X', 'X'],
            [' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X']
        ]
        sample_board.set_state(board_state, True)
        #test = sample_board.get_legal_moves()͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
        h = yourOpenEvalFn()
        print('OpenMoveEvalFn Test: This board has a score of %s.' % (h.score(sample_board, sample_board.get_active_player())))
    except NotImplementedError:
        print('OpenMoveEvalFn Test: Not implemented')
    except:
        print('OpenMoveEvalFn Test: ERROR OCCURRED')
        print(traceback.format_exc())

    print()

def beatRandom(yourAgent):

    """Example test you can run
    to make sure your AI does better
    than random."""

    print("")
    try:
        r = RandomPlayer()
        p = yourAgent()
        game = Board(p, r, 9, 9)
        output_b = game.copy()
        winner, move_history, termination = game.play_isolation(time_limit=5000, print_moves=True)
        print("\n", winner, " has won. Reason: ", termination)
        # Uncomment to see game͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
        # print game_as_text(winner, move_history, termination, output_b)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
    except NotImplementedError:
        print('CustomPlayer Test: Not Implemented')
    except:
        print('CustomPlayer Test: ERROR OCCURRED')
        print(traceback.format_exc())
    
    print()


def minimaxTest(yourAgent, minimax_fn):
    """Example test to make sure
    your minimax works, using the
    OpenMoveEvalFunction evaluation function.
    This can be used for debugging your code
    with different model Board states.
    Especially important to check alphabeta
    pruning"""

    # create dummy 9x9 board͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
    print("Now running Minimax test 1.")
    print()
    try:
        def time_left():  # For these testing purposes, let's ignore timeouts
            return 10000

        player = yourAgent() #using as a dummy player to create a board
        sample_board = Board(player, RandomPlayer())
        # setting up the board as though we've been playing͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
        board_state = [
            [' ', ' ', 'K1', 'X', 'X', 'X', ' ', ' ', ' '],
            ['X', ' ', ' ', 'X', ' ', 'X', ' ', 'X', ' '],
            [' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', ' '],
            ['X', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', ' ', ' ', 'X', 'K2', ' ', ' '],
            [' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
            [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        sample_board.set_state(board_state, True)

        test_pass = True

        expected_depth_scores = [(1, -3), (2, -2), (3, -1), (4, -1), (5, 0)]
        
        for depth, exp_score in expected_depth_scores:
            move, score = minimax_fn(player, sample_board, time_left, depth=depth, my_turn=True)
            if exp_score != score:
                print("Minimax failed for depth: ", depth)
                test_pass = False
            else:
                print("Minimax passed for depth: ", depth)

        if test_pass:
            print()
            print("Now running Minimax test 2.")
            print()
            player = yourAgent()
            sample_board = Board(RandomPlayer(),player)
            # setting up the board as though we've been playing͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄉͏󠄈͏︁
            board_state = [
                [' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' '],
                ['X', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' '],
                [' ', 'X', 'X', 'X', 'X', ' ', 'X', 'X', ' '],
                [' ', ' ', 'X', ' ', ' ', 'X', 'X', ' ', 'X'],
                [' ', ' ', 'X', 'X', 'X', 'X', 'K2', 'X', 'X'],
                [' ', ' ', ' ', 'K1', 'X', 'X', 'X', 'X', ' '],
                [' ', ' ', ' ', 'X', ' ', 'X', 'X', 'X', 'X'],
                [' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X'],
                [' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X', ' ']
            ]
            sample_board.set_state(board_state, p1_turn=True)

            test_pass = True

            expected_depth_scores = [(1, -1), (2, 1), (3, 0), (4, -2), (5, -3)]

            for depth, exp_score in expected_depth_scores:
                move, score = minimax_fn(player, sample_board, time_left, depth=depth, my_turn=False)
          
                if exp_score != score:
                    print("Minimax failed for depth: ", depth)
                    test_pass = False
                else:
                    print("Minimax passed for depth: ", depth)

        if test_pass:
            print("Minimax Test: Runs Successfully!")

        else:
            print("Minimax Test: Failed")

    except NotImplementedError:
        print('Minimax Test: Not implemented')
    except:
        print('Minimax Test: ERROR OCCURRED')
        print(traceback.format_exc())

def alphabetaTest(yourAgent, alphabeta_fn):
    """Improved test for AlphaBeta algorithm with specific board setups and expected scores.
    
    Args:
        yourAgent: The agent you are testing.
        alphabeta_fn: The alphabeta function to test.
    
    Returns:
        None
    """

    print("=== AlphaBeta Test: Starting ===")
    
    def time_left():
        return 10000  # No time constraints in testing

    # Test Case 1 - Set up for P1 to make optimal decision
    print("\nRunning AlphaBeta Test 1...\n")
    
    player = yourAgent()
    opponent = RandomPlayer()
    sample_board = Board(player, opponent)

    # Simple board state setup for Player 1
    board_state_1 = [
        [' ', ' ', 'K1', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    sample_board.set_state(board_state_1, True)

    expected_depth_scores_1 = [(1, -1), (2, -2), (3, 0), (4, 1), (5, 2)]
    test_pass_1 = True

    for depth, expected_score in expected_depth_scores_1:
        move, score = alphabeta_fn(player, sample_board, time_left, depth=depth, my_turn=True)
        if score != expected_score:
            print(f"AlphaBeta failed at depth {depth} (expected {expected_score}, got {score})")
            test_pass_1 = False
        else:
            print(f"AlphaBeta passed at depth {depth} (score: {score})")

    # Test Case 2 - Set up for Player 2 to make optimal decision
    print("\nRunning AlphaBeta Test 2...\n")

    player2 = yourAgent()
    sample_board_2 = Board(opponent, player2)

    # More complex board setup for Player 2
    board_state_2 = [
        [' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' '],
        [' ', ' ', 'X', ' ', ' ', ' ', 'X', ' ', ' '],
        [' ', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'X', ' ', 'K2', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', 'K1', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    sample_board_2.set_state(board_state_2, p1_turn=True)

    expected_depth_scores_2 = [(1, 0), (2, -1), (3, -2), (4, -1), (5, -3)]
    test_pass_2 = True

    for depth, expected_score in expected_depth_scores_2:
        move, score = alphabeta_fn(player2, sample_board_2, time_left, depth=depth, my_turn=False)
        if score != expected_score:
            print(f"AlphaBeta failed at depth {depth} (expected {expected_score}, got {score})")
            test_pass_2 = False
        else:
            print(f"AlphaBeta passed at depth {depth} (score: {score})")

    # Test summary
    if test_pass_1 and test_pass_2:
        print("\n=== AlphaBeta Test: All Tests Passed! ===")
    else:
        print("\n=== AlphaBeta Test: Some Tests Failed ===")
