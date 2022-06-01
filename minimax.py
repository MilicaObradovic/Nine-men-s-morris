from board import Board
import math
import time

class Game(object):
    def __init__(self):
        self.current_board = Board()
        self._player_turn = 'X'
        # self.arrayX = []
        # self.arrayY = []
        
    def next_player(self, previous):
        if previous == "X":
            self._player_turn = 'Y' 
        else:
            self._player_turn = 'X'

    def insert_validation(self, string, moving_faze, eating_faze):
        while True:
            s = input("Player " +self._player_turn+ " - insert "+string+": format - A1 > ")
            if len(s) == 2:
                break
            else:
                print("Input format is wrong")

        spot = [s[0], s[1]]
        lista = ["A", "B", "C", "D", "E", "F", "G"]
        wrong_letter = True
        wrong_number = False
        validation = True

        for i in range(len(lista)):
            if spot[0].upper() == lista[i]:
                spot[0] = i
                wrong_letter = False
                break
                
        if wrong_letter == True:
            print("Unavailable letter")
        try:
            spot[1] = int(spot[1])-1
        except ValueError:
            wrong_number = True

        if spot[1] not in [0,1,2,3,4,5,6]:
            wrong_number = True
            print("Unavailable number")
        
        if wrong_letter == False and wrong_number == False:
            if moving_faze == False and eating_faze == False:
                if self.current_board.get_value(spot[0],spot[1]) != ".":
                    return False, spot
                else:
                    return True, spot
            elif eating_faze == True:
                if self.current_board.get_value(spot[0],spot[1]) == self._player_turn:
                    print("Your morris.. try again")
                    return False, spot
                else:
                    return True, spot
            elif moving_faze == True:
                if self.current_board.get_value(spot[0],spot[1]) != self._player_turn:
                    return False, spot
                else:
                    return True, spot
        else:
            return False, spot

    def first_phase(self):
        first = 8
        while first > 0:

            if self._player_turn == "X":
                start = time.time()
                best , spot = self.minimax_first_phase(self.current_board, 4, True, -1, -1,-math.inf,math.inf)
                end = time.time()
                print('Evaluation time: '+str(round(end - start, 6)))
                # self.arrayX.append(spot)
                self.current_board.set_value(spot[0], spot[1], self._player_turn)
                print(self.current_board.arrayX)
                self.next_player(self._player_turn)
            print(self.current_board)
            print(30*"-")

            while True:
                validation, spot = self.insert_validation("spot", False, False)

                if validation == False:
                    print("Unavailable position.. try again")
                else:
                    self.current_board.set_value(spot[0], spot[1], self._player_turn)
                    # if self._player_turn == "X":
                    #     self.arrayX.append(spot)
                    # else:
                    #     self.arrayY.append(spot)

                    if self._player_turn == "X":
                        eating = self.current_board.closed_morris(self.current_board.arrayX, spot)
                    else:
                        eating = self.current_board.closed_morris(self.current_board.arrayY, spot)

                    self.eating_function(eating)
                    self.next_player(self._player_turn)
                    break
            first -= 1
        print(self.current_board)
        print(30*"-")
        print("Insert-faze is finished... Next is moving-faze")

    def delta(self, num, array1, array2, old1, old, new):
        if old1 in array1:
            delta = old -new
            if delta in array2:
                return True
            else:
                return False 
        else:
            return None

    def new_destination_validation(self, string, old_spot):
        validation, spot = self.insert_validation(string, False, False)
        if validation == True:
            if old_spot[0] != spot[0] and old_spot[1] != spot[1]:
                return False, spot
            elif old_spot[0] == spot[0]:
                # out
                check = self.delta(0,[0,6], [-3,3], old_spot[0], old_spot[1], spot[1])
                if check != None:
                    return check, spot
                # middle
                check = self.delta(0,[1,5], [-2,2], old_spot[0], old_spot[1], spot[1])
                if check != None:
                    return check, spot
                # in
                check = self.delta(0,[2,3,4], [-1,1], old_spot[0], old_spot[1], spot[1])
                if check != None:
                    return check, spot
            elif old_spot[1] == spot[1]:
                # out
                check = self.delta(1,[0,6], [-3,3], old_spot[1], old_spot[0], spot[0])
                if check != None:
                    return check, spot
                # middle
                check = self.delta(1,[1,5], [-2,2], old_spot[1], old_spot[0], spot[0])
                if check != None:
                    return check, spot
                # in
                check = self.delta(1,[2,3,4], [-1,1], old_spot[1], old_spot[0], spot[0])
                if check != None:
                    return check, spot
                
        else:
            return False, spot

    def selection(self, array):
        while True:
            validation, spot = self.insert_validation("new destination", False, False) 
            # print(validation)
            validate = False
            if validation == False:
                print("Unavailable position.. try again")
            else:
                for elem in array:
                    if spot[0] == elem[0] and spot[1] == elem[1]:
                        validate = True
                        break
                if validate == True:
                    break
                else:
                    print("You have choosen unavailable spot")
        return spot

    # def closed_morris(self, array, new_spot):
    #     x = 0
    #     y = 0
    #     third1x = 0
    #     third2x = 0
    #     third1y = 0
    #     third2y = 0

    #     for el in array:
    #         # elementi u istom redu
    #         if el[0] == new_spot[0]:
    #             x += 1
    #         # elementi u istoj koloni
    #         if el[1] == new_spot[1]:
    #             y += 1
    #         if new_spot[0] == 3 or new_spot[1] == 3:
    #             if new_spot[0] == 3 and el[0] == 3:
    #                 if new_spot[1] in [0,1,2]:
    #                     if el[1] in [0,1,2]:
    #                         third1x += 1
    #                 else:
    #                     if el[1] in [4, 5, 6]:
    #                         third2x += 1
    #             elif new_spot[1] == 3 and el[1] == 3:
    #                 if new_spot[0] in [0,1,2]:
    #                     if el[0] in [0,1,2]:
    #                         third1y += 1
    #                 else:
    #                     if el[0] in [4, 5, 6]:
    #                         third2y += 1

    #     if x > 2 and new_spot[0] == 3:
    #         if third1x == 3 or third2x == 3:
    #             return True
    #     elif y > 2 and new_spot[1] == 3:
    #         if third1y == 3 or third2y == 3:
    #             return True
    #     elif x == 3:
    #         return True
    #     elif y == 3:
    #         return True
    #     elif third1x == 3:
    #         return True
    #     elif third2x == 3:
    #         return True
    #     elif third1y == 3:
    #         return True
    #     elif third2y == 3:
    #         return True
    #     else:
    #         return False

    def all_morises(self, array):
        if len(array) < 3 or len(array) % 3 != 0:
            return False
        else:
            mistake = 0
            # print(array)
            for el in array:
                # print(el)
                closed = self.current_board.closed_morris(array, el)
                # print(closed)
                if closed == False:
                    mistake += 1
                    break
            # print("m"+str(mistake))
            if mistake == 0:
                return True
            else:
                return False

    def eating_option(self):
        while True:
            valid, spot = self.insert_validation("spot for eating", False, True)
            validation = False
            morises = False
            if valid == False:
                print("Unavailable position.. try again")
            elif self.current_board.get_value(spot[0],spot[1]) == ".":
                print("Empty spot.. try again")
            else:
                if self._player_turn == "X":
                    closed = self.current_board.closed_morris(self.current_board.arrayY, spot)
                else:
                    closed = self.current_board.closed_morris(self.current_board.arrayX, spot)
                if closed == True:
                    if self._player_turn == "X":
                        morises = self.all_morises(self.current_board.arrayY)
                    else:
                        morises = self.all_morises(self.current_board.arrayX)

                    if morises == True:
                        validation = True
                    else:
                        print("Choosen morris is closed.. try again")
                        
                else:
                    validation = True
            if validation == True:
                break
        return spot

    def eating_function(self, eating):
        if eating == True:
            print(self.current_board)
            print(30*"-")
            spot_for_eating = self.eating_option()
            self.current_board.set_value(spot_for_eating[0], spot_for_eating[1], ".")
            # if self._player_turn == "X":
            #     for el in self.current_board.arrayY:
            #         if spot_for_eating[0] == el[0] and spot_for_eating[1] == el[1]:
            #             self.current_board.arrayY.remove(el)
            #             break
            #     print(self.current_board.arrayY)
            # else:
            #     for el in self.current_board.arrayX:
            #         if spot_for_eating[0] == el[0] and spot_for_eating[1] == el[1]:
            #             self.current_board.arrayX.remove(el)
            #             break
            #     print(self.current_board.arrayX)

    def second_phase(self):
        while True:
            game_over = False
            print(self.current_board)
            print(30*"-")
            while True:
                validation, spot = self.insert_validation("spot you want to move", True, False)
                destinations = self.current_board.possible_destinations(spot)

                if validation == False:
                    print("Unavailable position.. try again")
                elif len(destinations) == 0:
                    print("Blocked piece")
                else:
                    break

            letters = ["A", "B", "C", "D", "E", "F", "G"]
            
            for el in destinations:
                el[0] = letters[el[0]]
                el[1] += 1

            rez = ""
            for el in destinations:
                rez += el[0]+str(el[1])+" "
            print("Possible spots: "+ rez)

            for el in destinations:
                el[0] = letters.index(el[0])
                el[1] -= 1
            
            new_spot = self.selection(destinations)

            self.current_board.set_value(new_spot[0], new_spot[1], self._player_turn)
            # if self._player_turn == "X":
            #     self.arrayX.append(new_spot)
            #     for el in self.arrayX:
            #         if spot[0] == el[0] and spot[1] == el[1]:
            #             self.arrayX.remove(el)
            #             break
            # else:
            #     self.arrayY.append(new_spot)
            #     for el in self.arrayY:
            #         if spot[0] == el[0] and spot[1] == el[1]:
            #             self.arrayY.remove(el)
            #             break

            self.current_board.set_value(spot[0], spot[1], ".")

            # poduslov ako se napravila mica mogucnost jedenja
            if self._player_turn == "X":
                eating = self.current_board.closed_morris(self.current_board.arrayX, new_spot)
            else:
                eating = self.current_board.closed_morris(self.current_board.arrayY, new_spot)

            self.eating_function(eating)
            if self._player_turn == "X":
                if len(self.current_board.arrayY) == 2:
                    game_over = True
            else:
                if len(self.current_board.arrayX) == 2:
                    game_over = True
            if game_over == True:
                break
                    
            self.next_player(self._player_turn)
            # uslov za izlazak iz druge faze je uslov za Game over

    def minimax_first_phase(self, state, depth, max_player, x, y, alpha, beta):
        if depth == 0:
            return state.evaluation_phase1(x,y)
            
        # player X
        if max_player:
            best = -math.inf
            bestMove = (-1,-1)
            for i in range(7):
                for j in range(7):
                    if state.get_value(i, j) == '.':
                        state.set_value(i, j, 'X')
                        move, spot= self.minimax_first_phase(state, depth-1, False, i , j, alpha, beta)
                        state.set_value(i, j, '.')
                        if move > best:
                            bestMove = spot
                            best = move
                    if best >= beta:
                        return best, bestMove

                    if best > alpha:
                        alpha = best
            return best, bestMove
        else:
            best = math.inf
            bestMove = (-1,-1)
            for i in range(7):
                for j in range(7):
                    if state.get_value(i, j) == '.':
                        state.set_value(i, j, 'Y')
                        move, spot= self.minimax_first_phase(state, depth-1, True, i, j, alpha, beta)
                        state.set_value(i, j, '.')
                        if move < best:
                            bestMove = spot
                            best = move
                    if best <= alpha:
                        return best, bestMove

                    if best < beta:
                        beta = best
            return best, bestMove
    
    def play(self):
        self.first_phase()

g = Game()
g.play()

# g.first_faze()
# g.second_faze()