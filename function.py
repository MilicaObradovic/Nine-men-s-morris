from copy import deepcopy

class Function(object):
    def actions_first_faze(self, state, piece):
        array = []
        for i in range(7):
            for j in range(7):
                board = deepcopy(state)
                if board.get_value(i,j) == ".":
                    # ide redom i postavlja figure
                    board.set_value(i, j, piece)
                    array.append(board)
        return array

    # def win(self, state, piece):
