import logging
import coloredlogs

from Coach import Coach
from tictactoe.TicTacToeGame import TicTacToeGame
from tictactoe.keras.NNet import NNetWrapper as nn
from utils import *

log = logging.getLogger(__name__)
coloredlogs.install(level='INFO')  # Change this to DEBUG to see more info.

args = DotDict({
    'num_iters': 1000,
    'num_eps': 100,
    'temp_threshold': 15,
    'update_threshold': 0.6,
    'max_len_of_queue': 200000,
    'num_mcts_sims': 25,
    'arena_compare': 40,
    'cpuct': 1,
    'checkpoint': './temp/',
    'load_model': False,
    'load_folder_file': ('/dev/models/8x100x50', 'best.pth.tar'),
    'num_iters_for_train_examples_history': 20,
})


def main():
    game = TicTacToeGame()

    log.info('Loading %s...', nn.__name__)
    neural_net = nn(game)

    if args.load_model:
        log.info('Loading checkpoint "%s/%s"...', args.load_folder_file)
        neural_net.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])
    else:
        log.warning('Not loading a checkpoint!')

    log.info('Loading the Coach...')
    coach = Coach(game, neural_net, args)

    if args.load_model:
        log.info("Loading 'train_examples' from file...")
        coach.load_train_examples()

    log.info('Starting the learning process 🎉')
    coach.learn()


if __name__ == "__main__":
    main()
