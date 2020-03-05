# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    
    def __init__(self, root: TreeNode):
        self.stack=[]
        self.add_left_most_in_stack(root)

    def add_left_most_in_stack(self, root):
        if root:
            self.stack.append(root)
            self.add_left_most_in_stack(root.left)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node=self.stack.pop()
        self.add_left_most_in_stack(node.right)
        return node.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()