import math
from binary_tree import BinaryTree


class BST(BinaryTree):
    def __init__(self, root):
        self.root = root

    def recoverBST(self, root):
        """
        Do not return anything, modify root in-place instead.
        related problem: 99. Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/
        """
        self.findMaxMinNode(root)

        def recoverBSTNode(root):
            if root:
                left = -math.inf
                right = math.inf
                if root.left:
                    left = root.left.max_node.val
                if root.right:
                    right = root.right.min_node.val
                if not(left < root.val and right > root.val):
                    temp = [left, root.val, right]
                    temp.sort()
                    if root.left:
                        root.left.max_node.val = temp[0]
                    if root.right:
                        root.right.min_node.val = temp[2]
                    root.val = temp[1]

        def recoverBSTRecursion(root):
            if root:
                recoverBSTRecursion(root.left)
                recoverBSTRecursion(root.right)
                recoverBSTNode(root)
        recoverBSTRecursion(root)

    def isValidBST(self, root):
        self.findMaxMinNode(root)

        def isValidBSTNode(root):
            if root:
                left = -math.inf
                right = math.inf
                if root.left:
                    left = root.left.max_node.val
                if root.right:
                    right = root.right.min_node.val
                if not(left < root.val and right > root.val):
                    return False
                else:
                    return True
            else:
                return True

        def isValidBSTRecursion(root):
            if root:
                return isValidBSTNode(root) and isValidBSTRecursion(root.left) and isValidBSTRecursion(root.right)
            else:
                return True
        return isValidBSTRecursion(root)
