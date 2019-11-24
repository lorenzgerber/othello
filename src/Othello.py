from MiniMaxAlgorithm import MiniMaxAlgorithm
from CountingEvaluator import CountingEvaluator
from HeuristicsEvaluator import HeuristicsEvaluator
from OthelloAction import OthelloAction
from sys import argv

def main():
    
    # Parsing and checking cli args
    if (len(argv) != 3):
        print("Usage: Othello.py <gameState> <time limit>")
 
    algorithm = MiniMaxAlgorithm()
    algorithm.set_search_depth(20)
    algorithm.set_time_limit(int(argv[2]))
    algorithm.set_evaluator(HeuristicsEvaluator())
    algorithm.parse_board_string(argv[1])
    action = algorithm.evaluate()
    if ( action != 'pass'):
        action = "".join(['(',str(action.row),',', str(action.col),')'])
    print(action)


if __name__ == "__main__":
    main()