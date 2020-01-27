from typing import NewType
from typing import List

TreeNode = NewType('TreeNode', int)


class TreeNode:
    def __init__(self, value):
        self._value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self._value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value: int) -> bool:
        if value < self._value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self._value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    # def convertToList(self,):
    #     def makeList2(self, aNode):
    #         if aNode is None:
    #             return []
    #         return self.makeList2(aNode.lChild) + [aNode.data] + self.makeList2(aNode.rChild)

    # another version of function above where we return BST object that is subtree starting from chosen value given that it exists.
    # Otherwise it returns zero.
    def searchBST(self, value):

        if value < self._value:
            if self.left is None:
                return None
            else:
                return self.left.searchBST(value)
        elif value > self._value:
            if self.right is None:
                return None
            else:
                return self.right.searchBST(value)
        return self

    def preorderTraversal(self, node: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return
            pre_order.append(node._value)
            dfs(node.left)
            dfs(node.right)

        pre_order = []
        dfs(node)
        return pre_order

    def height(self, node:TreeNode):
        if node is None:
            return 0
        else:
            height=max(self.height(node.left), self.height(node.right)) + 1
        return height

    #level order traversal

    def levelOrder(self, root):
        result = []
        self.helper(root, 0, result)
        return result

    def helper(self, root, level, result):
        if root is None:
            return
        if len(result) <= level:
            result.append([])
        result[level].append(root._value)
        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)




if __name__ == '__main__':
    bst = TreeNode(4)
    bst.insert(2).insert(1).insert(3).insert(7).insert(10)
    print(bst)
    # it would be nice if we could cast bst into list but list(bst) does not work.

    print(bst.contains(7))
    subbst = bst.searchBST(6)
    dfsTraversal = bst.preorderTraversal(node=bst)
    bstHeight=bst.height(node=bst)
    levelOrder=bst.levelOrder(root=bst)

print("end")
