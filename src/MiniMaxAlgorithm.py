from OthelloAlgorithm import OthelloAlgorithm
from OthelloAction import OthelloAction
from math import inf

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
        heuristic = self.max_value( self.start_position, -inf, +inf)

        # the immediate next move from current othello_position 
        # that resulted in the best heuristic shall be returned
        # as othello_action

        possible_moves = self.start_position.get_moves()
        return (possible_moves[0])

    def set_search_depth(self, depth):
        self.depth = depth
        print("set the depth")


    def max_value(self, othello_position, alpha, beta):
        print("max value")
        
        # if s is a leaf then (othello board is full)
        if (othello_position.check_is_leaf()):
            print('report utility')
            self.evaluator.evaluate.self(othello_position)
        
        value = -inf
        
        for child_move in othello_position.get_moves():
            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = max(value, self.min_value(new_position, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                # beta cutoff
                break
        
        return ( value )


    def min_value(self, othello_position, alpha, beta):
        print("min value")
        
        # if s is a leaf then (othello board is full)
        if (othello_position.check_is_leaf()):
            print('report utility')
            self.evaluator.evaluate.self(othello_position)

        value = +inf
        
        for child_move in othello_position.get_moves():
            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = min(value, self.max_value(new_position, alpha, beta))
            alpha = min(alpha, value)
            if alpha >= beta:
                # alpha cutoff
                break
        
        return ( value )