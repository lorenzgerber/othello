from MiniMaxAlgorithm import MiniMaxAlgorithm
from CountingEvaluator import CountingEvaluator
from StabilityCornerEvaluator import StabilityCornerEvaluator
from OthelloAction import OthelloAction
from OthelloPosition import OthelloPosition
from sys import argv

def main():
    
    # Parsing and checking cli args
    if (len(argv) != 3):
        print("Usage: Othello.py <gameState> <time limit>")
    
    position = OthelloPosition(argv[1])
    algorithm = MiniMaxAlgorithm()
    algorithm.set_search_depth(1)
    algorithm.set_time_limit(int(argv[2]))
    algorithm.set_evaluator(CountingEvaluator())
    action = algorithm.evaluate(position)
    if ( action != 'pass'):
        action = "".join(['(',str(action.row),',', str(action.col),')'])
    print(action)


if __name__ == "__main__":
    main()