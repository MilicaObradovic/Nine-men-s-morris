class Board(object):
    def __init__(self):
        self.arrayX = []
        self.arrayY = []
        self.board = [ ['.',"-","-",'.',"-","-",'.'],
                        ["-",'.',"-",'.',"-",'.',"-"],
                        ["-","-",'.','.','.',"-","-"],
                        ['.','.','.',"-",'.','.','.'],
                        ["-","-",'.','.','.',"-","-"],
                        ["-",'.',"-",'.',"-",'.',"-"],
                        ['.',"-","-",'.',"-","-",'.']]

    def get_arrayX(self):
        return self.arrayX

    def get_arrayY(self):
        return self.arrayY

    def get_value(self, i, j):
        return self.board[i][j]
    
    def set_value(self, i, j, value):
        if value == "X":
            self.arrayX.append([i,j])
        elif value == "Y":
            self.arrayY.append([i,j])
        elif value == ".":
            if self.board[i][j] == "X":
                for el in self.arrayX:
                    if i == el[0] and j == el[1]:
                        self.arrayX.remove(el)
            elif self.board[i][j] == "Y":
                for el in self.arrayY:
                    if i == el[0] and j == el[1]:
                        self.arrayY.remove(el)
        self.board[i][j] = value
        # print("X = ")
        # print(self.arrayX)
        # print("Y = ")
        # print(self.arrayY)

    def first_move(self):
        if len(self.arrayX) == 1:
            return True
        return False

    def possible_destinations(self, spot):
        lista = []
        numbers = [0,1,2,3,4,5,6]
        if spot[0] in [0,6] or spot[1] in [0,6]:
            for x in [-3,3]:
                lista.append([spot[0], spot[1]+x])
                lista.append([spot[0]+x, spot[1]])
        if spot[0] in [1,5] or spot[1] in [1,5]:
            for x in [-2,2]:
                lista.append([spot[0], spot[1]+x])
                lista.append([spot[0]+x, spot[1]])

        if spot[0] in [2,3,4] or spot[1] in [2,3,4]:
            for x in [-1,1]:
                lista.append([spot[0], spot[1]+x])
                lista.append([spot[0]+x, spot[1]])

        lista2 = []
        lista3 = []

        for elem in lista:
            if elem[0] in numbers and elem[1] in numbers:
                lista2.append(elem)

        for elem in lista2:
            if self.board[elem[0]][elem[1]] == ".":
                lista3.append(elem)
            
        return lista3

    def are_same(self, board):
        for i in range(7):
            for j in range(7):
                if self.board[i][j] != board[i][j]:
                    return False
        return True

    def best_opening(self):
        ret = 0
        spot = [-1, -1]
        if len(self.arrayX) == 1:
            for i in range(7):
                for j in range(7):
                    if self.board[i][j] != "." and self.board[i][j] != "-":
                        spot = [i, j]

            array = self.possible_destinations(spot)
            ret += len(array)
        return ret, spot

    def num_of_blocked(self, player):
        ret = 0
        for i in range(7):
            for j in range(7):
                if self.board[i][j] == player:
                    array = self.possible_destinations([i,j])
                    if len(array) == 0:
                        ret += 1

        return ret

    def diff_num_of_pieces(self):
        return len(self.arrayX) - len(self.arrayY)

    def diff_num_of_blocked(self):
        return self.num_of_blocked("Y") - self.num_of_blocked("X")

    def closed_morris(self, array, new_spot):
        x = 0
        y = 0
        third1x = 0
        third2x = 0
        third1y = 0
        third2y = 0

        for el in array:
            # elementi u istom redu
            if el[0] == new_spot[0]:
                x += 1
            # elementi u istoj koloni
            if el[1] == new_spot[1]:
                y += 1
            if new_spot[0] == 3 or new_spot[1] == 3:
                if new_spot[0] == 3 and el[0] == 3:
                    if new_spot[1] in [0,1,2]:
                        if el[1] in [0,1,2]:
                            third1x += 1
                    else:
                        if el[1] in [4, 5, 6]:
                            third2x += 1
                elif new_spot[1] == 3 and el[1] == 3:
                    if new_spot[0] in [0,1,2]:
                        if el[0] in [0,1,2]:
                            third1y += 1
                    else:
                        if el[0] in [4, 5, 6]:
                            third2y += 1

        if x > 2 and new_spot[0] == 3:
            if third1x == 3 or third2x == 3:
                return True
        elif y > 2 and new_spot[1] == 3:
            if third1y == 3 or third2y == 3:
                return True
        elif x == 3:
            return True
        elif y == 3:
            return True
        elif third1x == 3:
            return True
        elif third2x == 3:
            return True
        elif third1y == 3:
            return True
        elif third2y == 3:
            return True
        else:
            return False

    def morrises(self, array, x, y):
        array2 = []
        for i in range(8):
            array2.append(0)
        for el in array:
            if el[x] == 0:
                array2[0] += 1
            elif el[x] == 1:
                array2[1] += 1
            elif el[x] == 2:
                array2[2] += 1
            elif el[x] == 3 and el[y] in [0,1,2]:
                array2[3] += 1
            elif el[x] == 3 and el[y] in [4,5,6]:
                array2[4] += 1
            elif el[x] == 4:
                array2[5] += 1
            elif el[x] == 5:
                array2[6] += 1
            elif el[x] == 6:
                array2[7] += 1
        return array2

    def num_of_morrises(self, array, double_m):
        arrayX = self.morrises(array, 0, 1)
        arrayY = self.morrises(array, 1, 0)
        ret = 0
        array1 = []
        array2 = []
        for i in range(len(arrayX)):
            if arrayX[i] == 3:
                ret +=1
                array1.append(i)
        for j in range(len(arrayY)):
            if arrayY[j] == 3:
                ret +=1
                array2.append(j)

        if double_m:
            double = 0
            for el1 in array1:
                for el2 in array2:
                    if el1 == el2 and el1 in [0,1,2] and el2 in [0,1,2]:
                        double+=1
                    elif el1 == el2 and el1 in [5,6,7] and el2 in [5,6,7]: 
                        double+=1
                    elif el1 == 0 and el2 == 7:
                        double+=1
                    elif el2 == 0 and el1 == 7:
                        double+=1
                    elif el1 == 1 and el2 == 5:
                        double+=1
                    elif el2 == 1 and el1 == 5:
                        double+=1
                    elif el1 == 2 and el2 == 4:
                        double+=1
                    elif el2 == 2 and el1 == 4:
                        double+=1

            return double
        else:
            return ret

    def two_piece_config(self, array):
        arrayX = self.morrises(array, 0, 1)
        arrayY = self.morrises(array, 1, 0)
        ret = 0
        for el in arrayX:
            if el == 2:
                ret +=1
        for el in arrayY:
            if el == 2:
                ret +=1
            # print(ret)
        return ret

    def closed_moris_config(self, x, y):
        if self.closed_morris(self.arrayX, [x,y]):
            return 1
        elif self.closed_morris(self.arrayY, [x,y]):
            return -1
        else:
            return 0

    def diff_num_of_two_config(self):
        return self.two_piece_config(self.arrayX) - self.two_piece_config(self.arrayY)

    def diff_num_of_morrises(self):
        return self.num_of_morrises(self.arrayX, False) - self.num_of_morrises(self.arrayY, False)
        
    def double_morises(self):
        return self.num_of_morrises(self.arrayX, True) - self.num_of_morrises(self.arrayY, True)

    def evaluation_phase1(self, x, y):
        return 26 * self.diff_num_of_morrises()+\
            self.diff_num_of_blocked()+\
            9 * self.diff_num_of_pieces()+\
                    self.double_morises()+10 * self.diff_num_of_two_config() + 20 * self.closed_moris_config(x,y), (x,y)

    def __str__(self):
        ret = "\n"
        ret +="  1   2   3   4   5   6   7\n"
        ret +="A %s --------- %s --------- %s\n"% (self.board[0][0], self.board[0][3], self.board[0][6])
        ret +="  |           |           |\n"
        ret +="B |   %s ----- %s ----- %s   |\n"% (self.board[1][1], self.board[1][3], self.board[1][5])
        ret +="  |   |       |       |   |\n"
        ret +="C |   |   %s - %s - %s   |   |\n"% (self.board[2][2], self.board[2][3], self.board[2][4])
        ret +="  |   |   |       |   |   |\n"
        ret +="D %s - %s - %s       %s - %s - %s\n"% (self.board[3][0], self.board[3][1], self.board[3][2], self.board[3][4], self.board[3][5], self.board[3][6])
        ret +="  |   |   |       |   |   |\n"
        ret +="E |   |   %s - %s - %s   |   |\n"% (self.board[4][2], self.board[4][3], self.board[4][4])
        ret +="  |   |       |       |   |\n"
        ret +="F |   %s ----- %s ----- %s   |\n"% (self.board[5][1], self.board[5][3], self.board[5][5])
        ret +="  |           |           |\n"
        ret +="G %s --------- %s --------- %s\n"% (self.board[6][0], self.board[6][3], self.board[6][6])
        return ret


array = [[1,1], [1,3], [5,1], [3,1]]
b = Board()
# print(10 * b.diff_num_of_two_config())
