from OthelloAlgorithm import OthelloAlgorithm
from OthelloAction import OthelloAction
from math import inf
from time import time

class MiniMaxAlgorithm(OthelloAlgorithm):

    def __init__(self):
        self.depth = 10
        self.tree = []
        self.depth_step = 1
        self.time_limit = 10
        self.transpositions = {}



    def set_evaluator(self, othello_evaluator):
        self.evaluator = othello_evaluator

    def set_time_limit(self, time_limit):
        self.time_limit = time_limit

    def evaluate(self, othello_position):

        start_time = time()
        while True:
            self.start_position = othello_position.clone()
            heuristic = self.max_value( self.start_position, self.depth, -inf, +inf, '0,', self.transpositions ,start_time)
            if (time() - start_time >= self.time_limit):
                 break
            
            self.depth = self.depth + self.depth_step
        
        ordering = self.transpositions.get('0,')

        def get_key(item):
                return (item[1])

        if (ordering == None ):
            return ('pass')

        ordering = sorted(ordering, key=get_key,reverse=True)
        best_move = [x[0] for x in ordering][0]
        moves = othello_position.get_moves()
        return (moves[best_move])

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
            
            if (len(ordering) > len(moves) ):
                print(sequence)
                print(ordering)
                print(moves)

            ordering = sorted(ordering, key=get_key,reverse=True)
            ordering = [x[0] for x in ordering]
            sorted_order = []

        for move_id in ordering:

            child_move = moves[move_id]

            if (time() - start_time >= self.time_limit):
                break

            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = max(value, self.min_value(new_position, depth, alpha, beta, sequence + str(move_id) + ',', transpositions, start_time))
            sorted_order.append((move_id, value))
            
            if value >= beta:
                transpositions[sequence] = sorted_order
                return (value)

            alpha = max(alpha, value)

        transpositions[sequence] = sorted_order
        
        return ( value )


    def min_value(self, othello_position, depth, alpha, beta, sequence, transpositions, start_time):

        depth = depth - 1
        
        if (othello_position.check_is_leaf()):
            #othello_position.print_board()
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

            if (len(ordering) > len(moves) ):
                print(sequence)
                print(ordering)
                print(moves)

            ordering = sorted(ordering, key=get_key)
            ordering = [x[0] for x in ordering]
            sorted_order = []
        
        for move_id in ordering:

            child_move = moves[move_id]

            if (time() - start_time >= self.time_limit):
                #othello_position.print_board()
                break

            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = min(value, self.max_value(new_position, depth, alpha, beta, sequence + str(move_id) + ',', transpositions, start_time))
            sorted_order.append((move_id, value))
            
            if value <= alpha:
                transpositions[sequence] = sorted_order
                return (value)

            beta = min(beta, value)

        transpositions[sequence] = sorted_order
        
        return ( value )