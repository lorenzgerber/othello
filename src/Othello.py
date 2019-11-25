from MiniMaxAlgorithm import MiniMaxAlgorithm
from CountingEvaluator import CountingEvaluator
from HeuristicsEvaluator import HeuristicsEvaluator
from OthelloAction import OthelloAction
from OthelloPosition import OthelloPosition
from sys import argv, stderr, exit

def main():
    
    # Parsing and checking cli args
    if (len(argv) != 3):
        print("Usage: Othello.py <gameState> <time limit>", file=stderr)
        exit()

    if (len(argv[1])!= 65 ):
        print("Usage: game state string has to be 65 chars", file=stderr)
        exit()

    
    position = OthelloPosition(argv[1])
    algorithm = MiniMaxAlgorithm()
    algorithm.set_search_depth(10)
    algorithm.set_time_limit(int(argv[2]))
    algorithm.set_evaluator(HeuristicsEvaluator())
    action = algorithm.evaluate(position)
    if ( action != 'pass'):
        action = "".join(['(',str(action.row),',', str(action.col),')'])
    print(action)


if __name__ == "__main__":
    main()