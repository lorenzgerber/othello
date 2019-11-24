from OthelloAlgorithm import OthelloAlgorithm
from OthelloAction import OthelloAction
from math import inf
from time import time

class MiniMaxAlgorithm(OthelloAlgorithm):

    def __init__(self):
        self.depth = 1
        self.max_depth = inf
        self.tree = []
        self.depth_step = 1
        self.time_limit = 10
        self.transpositions = {}
        self.next_moves = []



    def set_evaluator(self, othello_evaluator):
        self.evaluator = othello_evaluator

    def set_time_limit(self, time_limit):
        self.time_limit = time_limit

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
                    self.max_value( self.start_position, self.depth, -inf, +inf, True, self.next_moves, start_time )
                    ordering = self.next_moves
                    ordering = sorted(ordering, key=get_key, reverse=False)
                else:
                    self.min_value( self.start_position, self.depth, -inf, +inf, True, self.next_moves, start_time ) 
                    ordering = self.next_moves
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
        
            for i in best_move_at_depth:
                if (isinstance(i, (OthelloAction)) == True):
                    result = i
        else:
            result = 'pass'
        #print(self.depth)
        #print(time() - start_time)

        return (result)

    def set_search_depth(self, depth):
        self.max_depth = depth


    def max_value(self, othello_position, depth, alpha, beta, top_level, next_moves, start_time):
        
        depth = depth - 0.5
        moves = othello_position.get_moves()

        if (othello_position.check_is_leaf() or depth == 0 or moves == []):
            value = self.evaluator.evaluate(othello_position)
            if (top_level == True):
                next_moves = [(0,value)]

            return (value)
        
        value = -inf

        for move_id in range(0, len(moves)):

            child_move = moves[move_id]
            if (time() - start_time >= self.time_limit):
                break
            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = max(value, self.min_value(new_position, depth, alpha, beta, False, [], start_time))
            
            if value >= beta:
                return ( value )

            alpha = max(alpha, value)

            if (top_level == True):
                next_moves.append((move_id, value))
        
        return ( value )


    def min_value(self, othello_position, depth, alpha, beta, top_level, next_moves, start_time):

        depth = depth - 0.5
        moves = othello_position.get_moves()
        
        if (othello_position.check_is_leaf() or depth == 0 or moves == []):
            value = self.evaluator.evaluate(othello_position)
            if (top_level == True):
                next_moves = [(0,value)]

            return (value)

        value = +inf
        
        for move_id in range(0, len(moves)):

            child_move = moves[move_id]

            if (time() - start_time >= self.time_limit):
                break

            new_position = othello_position.clone()
            new_position.make_move(child_move)
            value = min(value, self.max_value(new_position, depth, alpha, beta, False, [], start_time))
            
            if value <= alpha:
                return ( value )

            beta = min(beta, value)

            if (top_level == True):
                next_moves.append((move_id, value))

        return ( value )