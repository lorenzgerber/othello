from OthelloAlgorithm import OthelloAlgorithm
from OthelloAction import OthelloAction
from math import inf
from time import time
import logging

class MiniMaxAlgorithm(OthelloAlgorithm):

    def __init__(self):
        self.depth = 1
        self.max_depth = inf
        self.tree = []
        self.depth_step = 1
        self.time_limit = 10
        self.transpositions = {}
        self.logger = {}



    def set_evaluator(self, othello_evaluator):
        self.evaluator = othello_evaluator

    def set_time_limit(self, time_limit):
        self.time_limit = time_limit
    
    def set_logger(self, logger):
        self.logger = logger

    def evaluate(self, othello_position):

        # Helper function for tuple sorting
        def get_key(item):
            return (item[1])

        best_move_at_depth = []
        start_time = time()

        # make a list for the result of every depth search
        moves = othello_position.get_moves()
        if ( moves != []):
            while self.depth <= self.max_depth:
                
                # clone the position as it will be overwritten else
                self.start_position = othello_position.clone()

                # Max for White, Min for Black
                if (self.start_position.to_move() == True):
                    self.logger.debug("step into max value")
                    self.max_value( self.start_position, self.depth, -inf, +inf, '0,', self.transpositions ,start_time )
                    ordering = self.transpositions.get('0,')
                    ordering = sorted(ordering, key=get_key, reverse=True)
                else:
                    self.logger.debug("step into min value")
                    self.min_value( self.start_position, self.depth, -inf, +inf, '0,', self.transpositions, start_time ) 
                    ordering = self.transpositions.get('0,')
                    ordering = sorted(ordering, key=get_key, reverse=False)

                # determine index of best move
                best_move = [x[0] for x in ordering][0]

                #extract best move from moves and add to best move att depth list
                best_move_at_depth.append(moves[best_move])
                
                # manage time
                if (time() - start_time >= self.time_limit):
                    break
                
                # set new search depth
                self.depth = self.depth + self.depth_step

                self.logger.debug("current depth %d", self.depth)
                self.logger.debug("current run time %d", time() - start_time)
        
            for i in best_move_at_depth:
                if (isinstance(i, (OthelloAction)) == True):
                    result = i
        else:
            result = 'pass'
        

        return (result)

    def set_search_depth(self, depth):
        self.max_depth = depth


    def max_value(self, othello_position, depth, alpha, beta, sequence, transpositions, start_time):
        
        depth = depth - 1
        moves = othello_position.get_moves()
        self.logger.debug("number of moves in max_value %d" , len(moves) )

        if (othello_position.check_is_leaf() or depth == 0 or moves == []):
            value = self.evaluator.evaluate(othello_position)
            sorted_order = []
            sorted_order.append((0, value))
            transpositions[sequence] = sorted_order
            return (value)
        
        value = -inf

        

        # check if there is an ordering for the current sequece
        ordering = transpositions.get(sequence)
        if (ordering == None ):
            ordering = range(len(moves))
            sorted_order = []
        else:
            def get_key(item):
                return (item[1])

            # sort the values from high to low (Max)
            ordering = sorted(ordering, key=get_key,reverse=False)
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

        moves = othello_position.get_moves()
        self.logger.debug("number of moves in min_value %d" , len(moves) )
        
        if (othello_position.check_is_leaf() or depth == 0 or moves == []):
            value = self.evaluator.evaluate(othello_position)
            sorted_order = []
            sorted_order.append((0, value))
            transpositions[sequence] = sorted_order
            return (value)

        value = +inf

        

        # check if there is an ordering for the current sequece
        ordering = transpositions.get(sequence)
        if (ordering == None ):
            ordering = range(len(moves))
            sorted_order = []
        else:
            def get_key(item):
                return (item[1])

            # sort the values from low to high (min)
            ordering = sorted(ordering, key=get_key, reverse=True)
            ordering = [x[0] for x in ordering]
            sorted_order = []
        
        for move_id in ordering:

            child_move = moves[move_id]

            if (time() - start_time >= self.time_limit):
                break

            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = min(value, self.max_value(new_position, depth, alpha, beta, sequence + str(move_id) + ',', transpositions, start_time))
            sorted_order.append((move_id, value))
            
            if value <= alpha:
                transpositions[sequence] = sorted_order
                return ( value )

            beta = min(beta, value)

        transpositions[sequence] = sorted_order
        
        return ( value )