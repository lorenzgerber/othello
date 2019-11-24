from OthelloAlgorithm import OthelloAlgorithm
from OthelloAction import OthelloAction
from PositionHandler import PositionHandler
from math import inf
from time import time
import numpy as np

class MiniMaxAlgorithm(OthelloAlgorithm):

    def __init__(self):
        self.depth = 1
        self.max_depth = inf
        self.tree = []
        self.depth_step = 1
        self.time_limit = 10
        self.transpositions = {}

    def parse_board_string(self, board_str):
        self.BOARD_SIZE = 8
        self.max_player = True
        self.board = np.array([['E' for col in range(self.BOARD_SIZE + 2)] for row in range(self.BOARD_SIZE + 2)])
        if len(list(board_str)) >= 65:
            if board_str[0] == 'W':
                self.max_player = True
            else:
                self.max_player = False
            for i in range(1, len(list(board_str))):
                col = ((i - 1) % 8) + 1
                row = (i - 1) // 8 + 1
                # For convenience we use W and B in the board instead of X and O:
                if board_str[i] == 'X':
                    self.board[row][col] = 'B'
                elif board_str[i] == 'O':
                    self.board[row][col] = 'W'




    def set_evaluator(self, othello_evaluator):
        self.evaluator = othello_evaluator

    def set_time_limit(self, time_limit):
        self.time_limit = time_limit

    def evaluate(self):

        self.handler = PositionHandler()

        # Helper function for tuple sorting
        def get_key(item):
                return (item[1])


        best_move_at_depth = []
        start_time = time()

        # make a list for the result of every depth search
        moves = self.handler.get_moves(self.board, self.BOARD_SIZE, self.max_player)
        if ( moves != []):
            while self.depth <= self.max_depth:
                
                # clone the position as it will be overwritten else
                self.start_board = self.handler.clone(self.board)
                max_player = self.max_player

                # Max for White, Min for Black
                if (self.handler.to_move(self.max_player) == True):
                    self.max_value( self.start_board, max_player, self.depth, -inf, +inf, '0,', self.transpositions ,start_time )
                    ordering = self.transpositions.get('0,')
                    ordering = sorted(ordering, key=get_key, reverse=True)
                else:
                    self.min_value( self.start_board, max_player, self.depth, -inf, +inf, '0,', self.transpositions, start_time ) 
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
        
            for i in best_move_at_depth:
                if (isinstance(i, (OthelloAction)) == True):
                    result = i
        else:
            result = 'pass'
        print(self.depth)
        print(time() - start_time)

        return (result)

    def set_search_depth(self, depth):
        self.max_depth = depth


    def max_value(self, board, max_player, depth, alpha, beta, sequence, transpositions, start_time):
        
        depth = depth - 0.5
        moves = self.handler.get_moves(board, self.BOARD_SIZE, max_player)

        if (self.handler.check_is_leaf( board, self.BOARD_SIZE ) or depth == 0 or moves == []):
            value = self.evaluator.evaluate(board, self.BOARD_SIZE, max_player)
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

            new_board = self.handler.clone(board)
            self.handler.make_move(new_board, self.BOARD_SIZE, child_move, max_player)

            if (max_player == True):
                max_player = False
            else:
                max_player = True

            value = max(value, self.min_value(new_board, max_player, depth, alpha, beta, sequence + str(move_id) + ',', transpositions, start_time))
            sorted_order.append((move_id, value))
            
            if value >= beta:
                transpositions[sequence] = sorted_order
                return (value)

            alpha = max(alpha, value)

        transpositions[sequence] = sorted_order
        
        return ( value )


    def min_value(self, board, max_player, depth, alpha, beta, sequence, transpositions, start_time):

        depth = depth - 0.5

        moves = self.handler.get_moves(board, self.BOARD_SIZE, max_player)
        
        if ( self.handler.check_is_leaf( board, self.BOARD_SIZE ) or depth == 0 or moves == []):
            value = self.evaluator.evaluate(board, self.BOARD_SIZE, max_player)
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

            new_board = self.handler.clone(board)
            self.handler.make_move(new_board, self.BOARD_SIZE, child_move, max_player)
            
            if (max_player == True):
                max_player = False
            else:
                max_player = True

            value = min(value, self.max_value(new_board, max_player, depth, alpha, beta, sequence + str(move_id) + ',', transpositions, start_time))
            sorted_order.append((move_id, value))
            
            if value <= alpha:
                transpositions[sequence] = sorted_order
                return ( value )

            beta = min(beta, value)

        transpositions[sequence] = sorted_order
        
        return ( value )