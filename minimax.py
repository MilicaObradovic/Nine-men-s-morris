from board import Board
import math
import time

class Game(object):
    def __init__(self):
        self.current_board = Board()
        self._player_turn = 'X'
        
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
                if self.current_board.closed_morris2(self.current_board.get_arrayX(), spot):
                    val = self.current_board.possible_for_eating2(self.current_board.arrayY)[0]
                    self.current_board.set_value(val[0], val[1], ".")
                print(self.current_board.get_arrayX())
                self.next_player(self._player_turn)
            print(self.current_board)
            print(30*"-")

            while True:
                validation, spot = self.insert_validation("spot", False, False)

                if validation == False:
                    print("Unavailable position.. try again")
                else:
                    self.current_board.set_value(spot[0], spot[1], self._player_turn)
                   
                    if self._player_turn == "X":
                        eating = self.current_board.closed_morris2(self.current_board.get_arrayX(), spot)
                    else:
                        eating = self.current_board.closed_morris2(self.current_board.get_arrayY(), spot)

                    self.eating_function(eating)
                    self.next_player(self._player_turn)
                    break
            first -= 1
        print(self.current_board)
        print(30*"-")
        print("Insert-faze is finished... Next is moving-faze")

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
                    closed = self.current_board.closed_morris2(self.current_board.get_arrayY(), spot)
                else:
                    closed = self.current_board.closed_morris2(self.current_board.get_arrayX(), spot)
                if closed == True:
                    if self._player_turn == "X":
                        morises = self.current_board.all_morises(self.current_board.arrayY)
                    else:
                        morises = self.current_board.all_morises(self.current_board.arrayX)

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
            self.current_board.set_value(spot[0], spot[1], ".")

            # poduslov ako se napravila mica mogucnost jedenja
            if self._player_turn == "X":
                eating = self.current_board.closed_morris2(self.current_board.arrayX, new_spot)
            else:
                eating = self.current_board.closed_morris2(self.current_board.arrayY, new_spot)

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
                        if state.closed_morris2(state.get_arrayX(),[i,j]):
                            array_for_eating = state.possible_for_eating2(state.arrayY)

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
                        if state.closed_morris2(state.get_arrayY(),[i,j]):
                            array_for_eating = state.possible_for_eating2(state.arrayX)

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