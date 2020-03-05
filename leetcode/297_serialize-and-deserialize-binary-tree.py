# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: list
        """
        q = deque([])
        if root:
            q.append(root)
        result = []
        while q:
            now = q.popleft()
            if not now == None:
                result.append(now.val)
                q.append(now.left)
                q.append(now.right)
            else:
                result.append(None)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: list
        :rtype: TreeNode
        """
        '''
        nodes=[TreeNode(d) if not d==None else None for d in data]
        for n in nodes:
            if not n==None:
                n.left=n.right=-1 
        q=deque([])
        flag=0
        for i,d in enumerate(data):
            if q:
                if not q[0].left==-1:
                    q[0].right=nodes[i]
                    q.popleft()
                else:
                    q[0].left=nodes[i]
            if not nodes[i]==None:
                q.append(nodes[i])
        return nodes[0] if nodes else None'''
        if data:
            root = TreeNode(data[0])
            q = deque([root])
            idx = 1
            while idx < len(data) and q:
                temp = q.popleft()
                temp.left = TreeNode(
                    data[idx]) if data[idx] is not None else None
                temp.right = TreeNode(
                    data[idx+1]) if data[idx+1] is not None else None
                idx += 2
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
        else:
            root = None
        return root
