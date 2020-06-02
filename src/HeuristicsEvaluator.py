from OthelloEvaluator import OthelloEvaluator

class HeuristicsEvaluator(OthelloEvaluator):


    def __init__(self):
        self.value_corner = 10
        self.value_edge = 5
        self.value_one_off = -1
        self.value_stone = 1
        self.value_move = 1


    def evaluate(self, othello_position):
        
        self.position = othello_position


        # Check corners
        score -= self.__check_corner('W')
        score += self.__check_corner('B')
        
        # Check edges
        score -= self.__check_edges('W')
        score += self.__check_edges('B')

        # Check one square off edges
        #score += self.__check_one_offs('W')
        #score -= self.__check_one_offs('B')

        # Number of
        score += self.count_stones(self.position)

        # mobility
        #score += self.count_moves(self.position)

        return (score)

    def __check_corner(self, color):
        points_sum = 0
        if ( self.position.board[0][0] == color):
            points_sum =+ self.value_corner

        if ( self.position.board[0][self.position.BOARD_SIZE-1] == color):
            points_sum =+ self.value_corner
            
        if ( self.position.board[self.position.BOARD_SIZE-1][0] == color):
            points_sum =+ self.value_corner

        if ( self.position.board[self.position.BOARD_SIZE-1][self.position.BOARD_SIZE-1] == color):
            points_sum =+ self.value_corner
        
        return ( points_sum )

    def __check_edges(self, color):
        points_sum = 0
        for i in range(0, self.position.BOARD_SIZE - 1):
            if ( self.position.board[0][i] == color ):
                points_sum += self.value_edge

        for i in range(0, self.position.BOARD_SIZE - 1):
            if ( self.position.board[self.position.BOARD_SIZE-1][i] == color ):
                points_sum += self.value_edge

        for i in range(0, self.position.BOARD_SIZE - 1):
            if ( self.position.board[i][0] == color ):
                points_sum += self.value_edge

        for i in range(0, self.position.BOARD_SIZE - 1):
            if ( self.position.board[i][self.position.BOARD_SIZE-1] == color ):
                points_sum += self.value_edge
        
        return (points_sum)

    def __check_one_offs(self, color):

        points_sum = 0

        for i in range(2, self.position.BOARD_SIZE - 3):
            if ( self.position.board[1][i] == color ):
                points_sum += self.value_one_off

        for i in range(2, self.position.BOARD_SIZE - 3):
            if ( self.position.board[self.position.BOARD_SIZE-2][i] == color ):
                points_sum += self.value_one_off

        for i in range(1, self.position.BOARD_SIZE - 2):
            if ( self.position.board[i][1] == color ):
                points_sum += self.value_one_off

        for i in range(1, self.position.BOARD_SIZE - 2):
            if ( self.position.board[i][self.position.BOARD_SIZE-2] == color ):
                points_sum += self.value_one_off
        
        return (points_sum)

    def count_stones(self, othello_position):
        black_squares = 0
        white_squares = 0
        for row in othello_position.board:
            for item in row:
                if item == 'W':
                    white_squares += self.value_stone
                if item == 'B':
                    black_squares += self.value_stone
        return white_squares - black_squares

    def count_moves(self, othello_position):
        max_moves = 0
        min_moves = 0
         
        if(othello_position.maxPlayer == True):
            max_moves = len(othello_position.get_moves())
        else:
            min_moves = len(othello_position.get_moves())
        
        max_moves = max_moves * self.value_move
        min_moves = min_moves * self.value_move

        return max_moves - min_moves

