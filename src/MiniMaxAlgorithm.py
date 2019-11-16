from OthelloAlgorithm import OthelloAlgorithm
from OthelloAction import OthelloAction
from math import inf
from time import time

class MiniMaxAlgorithm(OthelloAlgorithm):

    def __init__(self):
        self.depth = 0
        self.tree = []
        self.depth_step = 1
        self.time_limit = 10
        self.move_order = {}



    def set_evaluator(self, othello_evaluator):
        self.evaluator = othello_evaluator

    def evaluate(self, othello_position):

        self.start_position = othello_position
        start_time = time()
        while True:
            heuristic = self.max_value( self.start_position, self.depth, -inf, +inf, start_time)
            print(self.depth)
            if (time() - start_time >= self.time_limit):
                 break
            
            self.depth = self.depth + self.depth_step
        
        
        possible_moves = self.start_position.get_moves()
        return (possible_moves[0])

    def set_search_depth(self, depth):
        self.depth = depth


    def max_value(self, othello_position, depth, alpha, beta, start_time):
        
        if (othello_position.check_is_leaf() or depth == 0):
            return (self.evaluator.evaluate(othello_position))
        
        value = -inf
        
        for child_move in othello_position.get_moves():

            if (time() - start_time >= self.time_limit):
                 break

            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = max(value, self.min_value(new_position, depth, alpha, beta, start_time))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        
        return ( value )


    def min_value(self, othello_position, depth, alpha, beta, start_time):

        depth = depth - 1
        
        if (othello_position.check_is_leaf()):
            return (self.evaluator.evaluate(othello_position))

        value = +inf
        
        for child_move in othello_position.get_moves():

            if (time() - start_time >= self.time_limit):
                 break

            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = min(value, self.max_value(new_position, depth, alpha, beta, start_time))
            alpha = min(alpha, value)
            if alpha >= beta:
                break
        
        return ( value )