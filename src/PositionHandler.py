import numpy as np
from OthelloAction import OthelloAction


class PositionHandler(object):
    """
    This class is used to represent game positions. It uses a 2-dimensional char array for the board
    and a Boolean to keep track of which player has the move.

    Author: Ola Ringdahl
    """

    move_steps = [(0,1), (1,1), (1,0), (1,-1), (-1,0), (-1,-1), (0,-1), (-1,1)]
       


    def make_move(self, board, board_size, action, max_player):
        """
        Perform the move suggested by the OhelloAction action and return the new position. Observe that this also
        changes the player to move next.
        :param action: The move to make as an OthelloAction
        :return: The OthelloPosition resulting from making the move action in the current position.
        """

        if not action.is_pass_move:
            if self.to_move(max_player):
                board[action.row][action.col] = 'W'
            else:
                board[action.row][action.col] = 'B'
               
            for i in PositionHandler.move_steps:
                outer_bound_color = board[action.row][action.col]
                current = (action.row + i[0], action.col + i[1])
                
                if ( board[current[0]][current[1]] != 'E' and board[current[0], current[1]] != outer_bound_color):
                    collect_list = []
                    exit_condition = False
                    
                    while not exit_condition:
                        
                        collect_list.append(current)
                        current = (current[0] + i[0], current[1]+ i[1])
                        
                        if ( board[current[0]][current[1]] == 'E' ):
                            exit_condition = True

                        if ( board[current[0], current[1]] == outer_bound_color ):
                            exit_condition = True
                        
                        if ( current[0] < 0 or current[1] < 0 ):
                            exit_condition = True

                        if ( current[0] > board_size - 1 or current[1] > board_size):
                            exit_condition = True


                    if ( board[current[0]][current[1]] == outer_bound_color):
                        for j in collect_list:
                            board[j[0]][j[1]] = outer_bound_color


        if ( max_player == True ):
            max_player = False
        else:
            max_player = True
        
        

    def get_moves(self, board, board_size, max_player):
        """
        Get all possible moves for the current position
        :return: A list of OthelloAction representing all possible moves in the position. If the
        list is empty, there are no legal moves for the player who has the move.
        """
        moves = []
        append = moves.append
        for i in range(board_size):
            for j in range(board_size):
                if self.__is_candidate(board, i + 1, j + 1) and self.__is_move(board, board_size, max_player, i + 1, j + 1):
                    append(OthelloAction(i + 1, j + 1))
        return moves

    def __is_candidate(self, board, row, col):
        """
        Check if a position is a candidate for a move (not empty and has a neighbour)
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is a candidate
        """
        if board[row][col] != 'E':
            return False
        if self.__has_neighbour(board, row, col):
            return True
        return False

    def __is_move(self, board, board_size, max_player,  row, col):
        """
        Check if it is possible to do a move from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if row < 1 or row > board_size or col < 1 or col > board_size:
            return False
        if self.__check_north(board, board_size, max_player, row, col):
            return True
        if self.__check_north_east(board, board_size, max_player, row, col):
            return True
        if self.__check_east(board, board_size, max_player, row, col):
            return True
        if self.__check_south_east(board, board_size, max_player, row, col):
            return True
        if self.__check_south(board, board_size, max_player, row, col):
            return True
        if self.__check_south_west(board, board_size, max_player, row, col):
            return True
        if self.__check_west(board, board_size, max_player, row, col):
            return True
        if self.__check_north_west(board, board_size, max_player, row, col):
            return True

    def __check_north(self, board, board_size, max_player, row, col):
        """
        Check if it is possible to do a move to the north from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(board, max_player, row - 1, col):
            return False
        i = row - 2
        while i > 0:
            if board[i][col] == 'E':
                return False
            if self.__is_own_square(board, max_player, i, col):
                return True
            i -= 1
        return False

    def __check_north_east(self, board, board_size, max_player, row, col):
        """
        Check if it is possible to do a move to the north east from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(board, max_player, row - 1, col + 1):
            return False
        i = 2
        while row - i > 0 and col + i <= board_size:
            if board[row - i][col + i] == 'E':
                return False
            if self.__is_own_square(board, max_player, row - i, col + i):
                return True
            i += 1
        return False

    def __check_north_west(self, board, board_size, max_player, row, col):
        """
        Check if it is possible to do a move to the north west from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(board, max_player, row - 1, col - 1):
            return False
        i = 2
        while row - i > 0 and col - i > 0:
            if board[row - i][col - i] == 'E':
                return False
            if self.__is_own_square(board, max_player, row - i, col - i):
                return True
            i += 1
        return False

    def __check_south(self, board, board_size, max_player, row, col):
        """
        Check if it is possible to do a move to the south from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(board, max_player, row + 1, col):
            return False
        i = row + 2
        while i <= board_size:
            if board[i][col] == 'E':
                return False
            if self.__is_own_square(board, max_player, i, col):
                return True
            i += 1
        return False

    def __check_south_east(self, board, board_size, max_player, row, col):
        """
        Check if it is possible to do a move to the south east from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(board, max_player, row + 1, col + 1):
            return False
        i = 2
        while row + i <= board_size and col + i <= board_size:
            if board[row + i][col + i] == 'E':
                return False
            if self.__is_own_square(board, max_player, row + i, col + i):
                return True
            i += 1
        return False

    def __check_south_west(self, board, board_size, max_player, row, col):
        """
        Check if it is possible to do a move to the south west from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(board, max_player, row + 1, col - 1):
            return False
        i = 2
        while row + i <= board_size and col - i > 0:
            if board[row + i][col - i] == 'E':
                return False
            if self.__is_own_square(board, max_player, row + i, col - i):
                return True
            i += 1
        return False

    def __check_west(self, board, board_size, max_player, row, col):
        """
        Check if it is possible to do a move to the west from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(board, max_player, row, col - 1):
            return False
        i = col - 2
        while i > 0:
            if board[row][i] == 'E':
                return False
            if self.__is_own_square( board, max_player, row, i):
                return True
            i -= 1
        return False

    def __check_east(self, board, board_size, max_player, row, col):
        """
        Check if it is possible to do a move to the east from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(board, max_player, row, col + 1):
            return False
        i = col + 2
        while i <= board_size:
            if board[row][i] == 'E':
                return False
            if self.__is_own_square( board, max_player, row, i):
                return True
            i += 1
        return False

    def __is_opponent_square(self, board, max_player, row, col):
        """
        Check if the position is occupied by the opponent
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if opponent square
        """
        if max_player and board[row][col] == 'B':
            return True
        if not max_player and board[row][col] == 'W':
            return True
        return False

    def __is_own_square(self, board, max_player, row, col):
        """
        Check if the position is occupied by the player
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it's your own square
        """
        if not max_player and board[row][col] == 'B':
            return True
        if max_player and board[row][col] == 'W':
            return True
        return False

    def __has_neighbour(self, board, row, col):
        """
        Check if the position has any non-empty squares
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if has neighbours
        """
        if board[row - 1][col] != 'E':
            return True
        if board[row - 1, col + 1] != 'E':
            return True
        if board[row - 1][col - 1] != 'E':
            return True
        if board[row][col - 1] != 'E':
            return True
        if board[row][col + 1] != 'E':
            return True
        if board[row + 1][col - 1] != 'E':
            return True
        if board[row + 1][col + 1] != 'E':
            return True
        if board[row + 1][col] != 'E':
            return True
        return False

    def to_move(self, max_player):
        """
        Check which player's turn it is
        :return: True if the first player (white) has the move, otherwise False
        """
        return max_player

    def clone(self, board):
        """
        Copy the current position
        :return: A new OthelloPosition, identical to the current one.
        """
        
        cloned_board = np.copy(board)
        return cloned_board

    def print_board(self, board):
        """
        Prints the current board. Do not use when running othellostart (it will crash)
        :return: Nothing
        """
        print(board)
        # print("ToMove: ", self.maxPlayer)

    def check_is_leaf(self, board, board_size):
        """
        Checks if the current othello board is a leaf
        :return: Boolean True for if the board is full
        """
        for i in range(0, board_size):
            col = i % 8 + 1
            row = i // 8 + 1
            if( board[row][col] == 'E'):
                return (False)
        return (True)
