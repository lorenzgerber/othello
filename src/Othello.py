from OthelloAlgorithm import OthelloAlgorithm, MiniMaxAlgorithm
from OthelloEvaluator import OthelloEvaluator, StabilityCornerEvaluator
from sys import argv

def main():
    
    # Parsing and checking cli args
    if (len(argv) != 3):
        print("Usage: Othello.py <gameState> <time limit>")
    
    othello_position = argv[1]

    evaluator = StabilityCornerEvaluator()
    algorithm = MiniMaxAlgorithm()
    algorithm.set_evaluator(evaluator)
    algorithm.evaluate(othello_position)









if __name__ == "__main__":
    main()