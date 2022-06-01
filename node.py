from function import Function

class Node(object):
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth

    def __str__(self):
        # str(board)
        return str(self.state)

    def seen(self, state):
        temp = self.parent
        while temp != None:
            if temp.are_same(state) == True:
                return True
            temp = self.parent
        return False

    def children_first_faze(self, piece):
        funct = Function()
        actions = funct.actions_first_faze(self.state, piece)
        array = []
        for state in actions:
            node = Node(state, self, self.depth+1)
            array.append(node)
        return array