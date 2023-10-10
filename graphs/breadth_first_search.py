class Node:
    def __init__(self, name):
        self.name = name 
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
    
    def breadthSearchFirst(self, array):
        queue = [self]
        while len(queue) > 0:
            current_node = queue.pop(0)
            array.append(current_node.name)
            for child in current_node.children:
                queue.append(child)
        return array     