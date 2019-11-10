from OthelloAlgorithm import OthelloAlgorithm
from OthelloAction import OthelloAction

class MiniMaxAlgorithm(OthelloAlgorithm):

    def __init__(self):
        self.depth = 10

    def set_evaluator(self, othello_evaluator):
        self.evaluator = othello_evaluator
        print("I have set the othello_evaluator")

    def evaluate(self, othello_position):

        self.start_position = othello_position

        print("evaluating")
        # Here comes the MiniMax algorithm that will
        # call for the self.evaluator.evaluate to get
        # the heuristic

        

        heuristic = self.evaluator.evaluate(self.start_position)

        # the immediate next move from current othello_position 
        # that resulted in the best heuristic shall be returned
        # as othello_action

        possible_moves = self.start_position.get_moves()
        return (possible_moves[0])

    def set_search_depth(self, depth):
        self.depth = depth
        print("set the depth")


    def max_value(self):
        print("max value")

    def min_value(self):
        print("min value")