from OthelloEvaluator import OthelloEvaluator
from PositionHandler import PositionHandler

class HeuristicsEvaluator(OthelloEvaluator):


    def __init__(self):
        self.value_corner = 30
        self.value_edge = 20
        self.value_one_off = -5
        self.value_stone = 10
        self.value_move = 5


    def evaluate(self, board, board_size, max_player):
        
        self.board = board
        self.board_size = board_size
        self.max_player = max_player
        self.handler = PositionHandler()

        # Check corners
        score = self.__check_corner('W')
        score -= self.__check_corner('B')
        
        # Check edges
        score += self.__check_edges('W')
        score -= self.__check_edges('B')

        # Check one square off edges
        score += self.__check_one_offs('W')
        score -= self.__check_one_offs('B')

        # Number of
        score += self.count_stones()

        # mobility
        score += self.count_moves()

        return (score)

    def __check_corner(self, color):
        points_sum = 0
        if ( self.board[0][0] == color):
            points_sum =+ self.value_corner

        if ( self.board[0][self.board_size-1] == color):
            points_sum =+ self.value_corner
            
        if ( self.board[self.board_size-1][0] == color):
            points_sum =+ self.value_corner

        if ( self.board[self.board_size-1][self.board_size-1] == color):
            points_sum =+ self.value_corner
        
        return ( points_sum )

    def __check_edges(self, color):
        points_sum = 0
        for i in range(1, self.board_size - 2):
            if ( self.board[0][i] == color ):
                points_sum += self.value_edge

        for i in range(1, self.board_size - 2):
            if ( self.board[self.board_size-1][i] == color ):
                points_sum += self.value_edge

        for i in range(1, self.board_size - 2):
            if ( self.board[i][0] == color ):
                points_sum += self.value_edge

        for i in range(1, self.board_size - 2):
            if ( self.board[i][self.board_size-1] == color ):
                points_sum += self.value_edge
        
        return (points_sum)

    def __check_one_offs(self, color):

        points_sum = 0

        for i in range(2, self.board_size - 3):
            if ( self.board[1][i] == color ):
                points_sum += self.value_one_off

        for i in range(2, self.board_size - 3):
            if ( self.board[self.board_size-2][i] == color ):
                points_sum += self.value_one_off

        for i in range(1, self.board_size - 2):
            if ( self.board[i][1] == color ):
                points_sum += self.value_one_off

        for i in range(1, self.board_size - 2):
            if ( self.board[i][self.board_size-2] == color ):
                points_sum += self.value_one_off
        
        return (points_sum)

    def count_stones(self):
        black_squares = 0
        white_squares = 0
        for row in self.board:
            for item in row:
                if item == 'W':
                    white_squares += self.value_stone
                if item == 'B':
                    black_squares += self.value_stone
        return white_squares - black_squares

    def count_moves( self ):
         
        if(self.max_player == True):
            max_moves = len(self.handler.get_moves(self.board, self.board_size, self.max_player))
            self.max_player = False
            min_moves = len(self.handler.get_moves(self.board, self.board_size, self.max_player))
            self.max_player = True
        else:
            min_moves = len(self.handler.get_moves(self.board, self.board_size, self.max_player))
            self.max_player = True
            max_moves = len(self.handler.get_moves(self.board, self.board_size, self.max_player))
            self.max_player = False
        
        max_moves = max_moves * self.value_move
        min_moves = min_moves * self.value_move

        return max_moves - min_moves

