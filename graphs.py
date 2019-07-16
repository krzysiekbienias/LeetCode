#from binarytree import Node

class Node:

    def __init__(self,name):
        self.children=[]#list of objects "node"
        self._name=name

    def add_child(self,name):
        self.children.append(Node(name))
        return self

    def depth_first_search(self,array):
        array.append(self._name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array



root=Node(name="A")
root.add_child(name="B").add_child(name='C').add_child(name='C')
root.children[0].add_child(name="E").add_child(name='F')
root.children[2].add_child(name="G").add_child(name='H')
root.children[0].children[1].add_child(name="I").add_child(name='J')
root.children[2].children[0].add_child(name="I").add_child(name='J')


#BST Construction
class BST:
    def __init__(self,value):
        self._value=value
        self._left=None
        self._right=None
        




# print(root)

print("end")