from OthelloAlgorithm import OthelloAlgorithm
from OthelloAction import OthelloAction
from math import inf
from time import time

class MiniMaxAlgorithm(OthelloAlgorithm):

    def __init__(self):
        self.depth = 0
        self.tree = []
        self.depth_step = 1
        self.time_limit = 100000
        self.transpositions = {}



    def set_evaluator(self, othello_evaluator):
        self.evaluator = othello_evaluator

    def evaluate(self, othello_position):

        self.start_position = othello_position
        start_time = time()
        while True:
            heuristic = self.max_value( self.start_position, self.depth, -inf, +inf, "0", self.transpositions ,start_time)
            print(heuristic)
            if (time() - start_time >= self.time_limit):
                 break
            
            self.depth = self.depth + self.depth_step
        
        
        possible_moves = self.start_position.get_moves()
        return (possible_moves[0])

    def set_search_depth(self, depth):
        self.depth = depth


    def max_value(self, othello_position, depth, alpha, beta, sequence, transpositions, start_time):
        
        if (othello_position.check_is_leaf() or depth == 0):
            return (self.evaluator.evaluate(othello_position))
        
        value = -inf

        moves = othello_position.get_moves()

        # check if there is an ordering for the current sequece
        ordering = transpositions.get(sequence)
        if (ordering == None ):
            ordering = range(len(moves))
            sorted_order = []
        else:
            def get_key(item):
                return (item[1])

            ordering = sorted(ordering, key=get_key,reverse=True)
            ordering = [x[0] for x in ordering]
            sorted_order = []




        for move_id in ordering:

            child_move = moves[move_id]

            if (time() - start_time >= self.time_limit):
                    break

            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = max(value, self.min_value(new_position, depth, alpha, beta, sequence + str(move_id), transpositions, start_time))
            sorted_order.append((move_id, value))
            alpha = max(alpha, value)
            if alpha >= beta:
                transpositions[sequence] = sorted_order
                break

        transpositions[sequence] = sorted_order
        
        return ( value )


    def min_value(self, othello_position, depth, alpha, beta, sequence, transpositions, start_time):

        depth = depth - 1
        
        if (othello_position.check_is_leaf()):
            return (self.evaluator.evaluate(othello_position))

        value = +inf

        moves = othello_position.get_moves()

        # check if there is an ordering for the current sequece
        ordering = transpositions.get(sequence)
        if (ordering == None ):
            ordering = range(len(moves))
            sorted_order = []
        else:
            def get_key(item):
                return (item[1])

            ordering = sorted(ordering, key=get_key)
            ordering = [x[0] for x in ordering]
            sorted_order = []
        


        for move_id in ordering:

            child_move = moves[move_id]

            if (time() - start_time >= self.time_limit):
                 break

            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = min(value, self.max_value(new_position, depth, alpha, beta, sequence + str(move_id), transpositions, start_time))
            alpha = min(alpha, value)
            if alpha >= beta:
                transpositions[sequence] = sorted_order
                break

            transpositions[sequence] = sorted_order
        
        return ( value )