# def possible_for_eating(self, array):
    #     double = self.num_of_morrises(array, True)
    #     arrayX = self.morrises(array, 0, 1)
    #     arrayY = self.morrises(array, 1, 0)
    #     print(arrayX)
    #     print(arrayY)
    #     num_of_morrises = 0
    #     num_of_free = 0
    #     for el in arrayX:
    #         if el == 3:
    #             num_of_morrises +=1
    #         elif el != 0:
    #             num_of_free +=el
    #     for el in arrayY:
    #         if el == 3:
    #             num_of_morrises +=1
    #         elif el != 0:
    #             num_of_free +=el

    #     if num_of_morrises > 0:
    #         num_of_free -= 3*num_of_morrises
    #         if double >0:
    #             num_of_free += double

    #     print(num_of_morrises)
    #     print(num_of_free)
    #     if num_of_morrises > 0 and num_of_free == 0:
    #         return array
    #     elif num_of_morrises == 0:
    #         return array
    #     else:
    #         # vrati samo one van morrisa
    #         x = []
    #         y = []
    #         for i in range(len(arrayX)):
    #             if arrayX[i] == 3:
    #                 x.append(i)
    #         for i in range(len(arrayY)):
    #             if arrayY[i] == 3:
    #                 y.append(i)
            
    #         final_array = []
    #         final_array2 = []
    #         print(x)
    #         print(y)
    #         if len(x) != 0 and len(y) != 0:
    #             for i in range(len(array)):
    #                 if array[i][0] < 3 and array[i][0] not in x :
    #                     final_array2.append(array[i])
    #                 elif array[i][0] == 3 and array[i][1] in [0,1,2] and 3 not in x:
    #                     final_array2.append(array[i])
    #                 elif array[i][0] == 3 and array[i][1] in [4,5,6] and 4 not in x:
    #                     final_array2.append(array[i])
    #                 elif array[i][0] > 3 and (array[i][0]+1) not in x:
    #                     final_array2.append(array[i])
    #             for i in range(len(final_array2)):
    #                 if final_array2[i][1] < 3 and final_array2[i][1] not in y :
    #                     final_array.append(final_array2[i])
    #                 elif final_array2[i][1] == 3 and final_array2[i][0] in [0,1,2] and 3 not in y:
    #                     final_array.append(final_array2[i])
    #                 elif final_array2[i][1] == 3 and final_array2[i][0] in [4,5,6] and 4 not in y:
    #                     final_array.append(final_array2[i])
    #                 elif final_array2[i][1] > 3 and (final_array2[i][1]+1) not in y:
    #                     final_array.append(final_array2[i])
    #         elif len(y) != 0:
    #             for i in range(len(array)):
    #                 if array[i][1] < 3 and array[i][1] not in y :
    #                     final_array.append(array[i])
    #                 elif array[i][1] == 3 and array[i][0] in [0,1,2] and 3 not in y:
    #                     final_array.append(array[i])
    #                 elif array[i][1] == 3 and array[i][0] in [4,5,6] and 4 not in y:
    #                     final_array.append(array[i])
    #                 elif array[i][1] > 3 and (array[i][1]+1) not in y:
    #                     final_array.append(array[i])
    #         elif len(x) != 0:
    #             for i in range(len(array)):
    #                 if array[i][0] < 3 and array[i][0] not in x :
    #                     final_array.append(array[i])
    #                 elif array[i][0] == 3 and array[i][1] in [0,1,2] and 3 not in x:
    #                     final_array.append(array[i])
    #                 elif array[i][0] == 3 and array[i][1] in [4,5,6] and 4 not in x:
    #                     final_array.append(array[i])
    #                 elif array[i][0] > 3 and (array[i][0]+1) not in x:
    #                     final_array.append(array[i])

    #         return final_array


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


    # def delta(self, num, array1, array2, old1, old, new):
    #     if old1 in array1:
    #         delta = old -new
    #         if delta in array2:
    #             return True
    #         else:
    #             return False 
    #     else:
    #         return None

    # def new_destination_validation(self, string, old_spot):
    #     validation, spot = self.insert_validation(string, False, False)
    #     if validation == True:
    #         if old_spot[0] != spot[0] and old_spot[1] != spot[1]:
    #             return False, spot
    #         elif old_spot[0] == spot[0]:
    #             # out
    #             check = self.delta(0,[0,6], [-3,3], old_spot[0], old_spot[1], spot[1])
    #             if check != None:
    #                 return check, spot
    #             # middle
    #             check = self.delta(0,[1,5], [-2,2], old_spot[0], old_spot[1], spot[1])
    #             if check != None:
    #                 return check, spot
    #             # in
    #             check = self.delta(0,[2,3,4], [-1,1], old_spot[0], old_spot[1], spot[1])
    #             if check != None:
    #                 return check, spot
    #         elif old_spot[1] == spot[1]:
    #             # out
    #             check = self.delta(1,[0,6], [-3,3], old_spot[1], old_spot[0], spot[0])
    #             if check != None:
    #                 return check, spot
    #             # middle
    #             check = self.delta(1,[1,5], [-2,2], old_spot[1], old_spot[0], spot[0])
    #             if check != None:
    #                 return check, spot
    #             # in
    #             check = self.delta(1,[2,3,4], [-1,1], old_spot[1], old_spot[0], spot[0])
    #             if check != None:
    #                 return check, spot
                
    #     else:
    #         return False, spot