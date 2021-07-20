from game import Game
from aiPlayer import AIPlayer
from randomPlayer import RandomPlayer
from humanPlayer import HumanPlayer

if __name__ == "__main__":
    # 4 false 135/150
    # 5 false 49/50
    # 5 10 40 
    # 8 6

    black_player = HumanPlayer("X")
    # black_player = RandomPlayer("X")
    config_1 = {
    'search_depth': 6,
    'pre_search_flag': False,
    'pre_search_branch': 10,}
    white_player = AIPlayer("O", config_1)

    # # black_player = HumanPlayer("X")
    # black_player = AIPlayer("X")
    # white_player = AIPlayer("O")

    # for _ in range(50):
    #     game = Game(black_player, white_player)
    #     game.run()
    game = Game(black_player, white_player)
    game.run()
