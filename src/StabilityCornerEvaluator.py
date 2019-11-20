from OthelloEvaluator import OthelloEvaluator

class StabilityCornerEvaluator(OthelloEvaluator):

    def evaluate(self, othello_position):
        
        self.position = othello_position


        # Check corners
        score = self.__check_corner('X')
        score -= self.__check_corner('O')
        
        # Check edges
        score += self.__check_edges('X')
        score -= self.__check_edges('O')

        # Check one square off edges
        score += self.__check_one_offs('X')
        score -= self.__check_one_offs('O')

        return (score)

    def __check_corner(self, color):
        points_sum = 0
        if ( self.position.board[0][0] == color):
            points_sum =+ 3

        if ( self.position.board[0][self.position.BOARD_SIZE-1] == color):
            points_sum =+ 3
            
        if ( self.position.board[self.position.BOARD_SIZE-1][0] == color):
            points_sum =+ 3

        if ( self.position.board[self.position.BOARD_SIZE-1][self.position.BOARD_SIZE-1] == color):
            points_sum =+ 3
        
        return ( points_sum )

    def __check_edges(self, color):
        points_sum = 0
        for i in range(1, self.position.BOARD_SIZE - 2):
            if ( self.position.board[0][i] == color ):
                points_sum += 2

        for i in range(1, self.position.BOARD_SIZE - 2):
            if ( self.position.board[self.position.BOARD_SIZE-1][i] == color ):
                points_sum += 2

        for i in range(1, self.position.BOARD_SIZE - 2):
            if ( self.position.board[i][0] == color ):
                points_sum += 2

        for i in range(1, self.position.BOARD_SIZE - 2):
            if ( self.position.board[i][self.position.BOARD_SIZE-1] == color ):
                points_sum += 2
        
        return (points_sum)

    def __check_one_offs(self, color):

        points_sum = 0

        for i in range(2, self.position.BOARD_SIZE - 3):
            if ( self.position.board[1][i] == color ):
                points_sum -= 1

        for i in range(2, self.position.BOARD_SIZE - 3):
            if ( self.position.board[self.position.BOARD_SIZE-2][i] == color ):
                points_sum -= 1

        for i in range(1, self.position.BOARD_SIZE - 2):
            if ( self.position.board[i][1] == color ):
                points_sum -= 1

        for i in range(1, self.position.BOARD_SIZE - 2):
            if ( self.position.board[i][self.position.BOARD_SIZE-2] == color ):
                points_sum -= 1
        
        return (points_sum)
