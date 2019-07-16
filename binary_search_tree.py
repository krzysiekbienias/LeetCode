from typing import NewType

#TreeNode=NewType('TreeNode',int)


class TreeNode:
    def __init__(self,value):
        self._value=value
        self.left=None
        self.right=None

    def insert (self,value):
        if value<self._value:
            if self.left is None:
                self.left=TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right=TreeNode(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value: int) ->bool:
        if value<self._value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value>self._value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    #another version of function above where we return BST object that is subtree starting from chosen value given that it exists.
    # Otherwise it returns zero.
    def searchBST(self,value):

        if value < self._value:
            if self.left is None:
                return None
            else:
                return self.left.searchBST(value)
        elif value>self._value:
            if self.right is None:
                return None
            else:
                return self.right.searchBST(value)
        return self







##################################################################################
bst=TreeNode(4)
bst.insert(2).insert(1).insert(3).insert(7)
print(bst.contains(7))
subbst=bst.searchBST(6)

print("end")