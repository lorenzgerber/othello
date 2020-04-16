from MiniMaxAlgorithm import MiniMaxAlgorithm
from CountingEvaluator import CountingEvaluator
from HeuristicsEvaluator import HeuristicsEvaluator
from OthelloAction import OthelloAction
from OthelloPosition import OthelloPosition
from sys import argv, stderr, exit
import logging

def main():

    # create logger
    logger = logging.getLogger('othello')
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # Parsing and checking cli args
    if (len(argv) != 3):
        print("Usage: Othello.py <gameState> <time limit>", file=stderr)
        exit()

    if (len(argv[1])!= 65 ):
        print("Usage: game state string has to be 65 chars", file=stderr)
        exit()

    
    position = OthelloPosition(argv[1])
    algorithm = MiniMaxAlgorithm()
    algorithm.set_logger(logger)
    algorithm.set_search_depth(10)
    algorithm.set_time_limit(int(argv[2]))
    algorithm.set_evaluator(HeuristicsEvaluator())
    action = algorithm.evaluate(position)
    if ( action != 'pass'):
        action = "".join(['(',str(action.row),',', str(action.col),')'])
    print(action)


if __name__ == "__main__":
    main()