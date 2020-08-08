import math
from collections import deque


class BinaryTreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def inorderTraversal(self, root):
        '''
        related problem: 94. Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/
        '''
        if root:
            return self.inorderTraversal(root.left) + \
                [root.val] + \
                self.inorderTraversal(root.right)
        else:
            return []

    def postorderTraversal(self, root):
        '''
        145. Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/
        '''
        if root:
            return self.postorderTraversal(root.left) + \
                self.postorderTraversal(root.right) + \
                [root.val]
        else:
            return []

    def preorderTraversal(self, root):
        '''
        144. Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/
        '''
        if root:
            return ([root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right))
        else:
            return []

    def levelOrder(self, root):
        '''
        102. Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/
        '''
        if not root:
            return []
        result = []
        q = deque([(root, 1)])
        level_result = []
        while q:
            #print([(i[0].val,i[1]) for i in q])
            node = q.popleft()
            if node[0].left:
                q.append((node[0].left, node[1]+1))
            if node[0].right:
                q.append((node[0].right, node[1]+1))
            if q and node[1] == q[0][1]:
                level_result.append(node[0].val)
            else:
                level_result.append(node[0].val)
                result.append(level_result)
                level_result = []
        return result

    def findMaxMinNode(self, root):
        if root:
            l_max, l_min = self.findMaxMinNode(root.left)
            r_max, r_min = self.findMaxMinNode(root.right)

            def get_root_MaxMin(root, func, inf_v, l_m, r_m):
                l_m_v = l_m.val if l_m else inf_v
                r_m_v = r_m.val if r_m else inf_v
                m_v = func([l_m_v, r_m_v, root.val])
                if m_v == root.val:
                    return root
                elif m_v == l_m_v:
                    return root.left
                else:
                    return root.right
            root.max_node, root.min_node = root, root
            root.max_node = get_root_MaxMin(
                root, max, -math.inf, l_max, r_max).max_node
            root.min_node = get_root_MaxMin(
                root, min, math.inf, l_min, r_min).min_node
            return root.max_node, root.min_node
        else:
            return None, None

    def isSameTree(self, p, q):
        '''
        100. Same Tree - https://leetcode.com/problems/same-tree/
        '''
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: BinaryTreeNode
        :rtype: list
        297. Serialize and Deserialize Binary Tree - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
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
        :rtype: BinaryTreeNode
        """
        '''
        nodes=[BinaryTreeNode(d) if not d==None else None for d in data]
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
            root = BinaryTreeNode(data[0])
            q = deque([root])
            idx = 1
            while idx < len(data) and q:
                temp = q.popleft()
                temp.left = BinaryTreeNode(
                    data[idx]) if data[idx] is not None else None
                temp.right = BinaryTreeNode(
                    data[idx+1]) if data[idx+1] is not None else None
                idx += 2
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
        else:
            root = None
        return root

    def maxPathSum(self, root):
        '''
        124. Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/
        '''
        self.maxPathSum_result = -math.inf
        self.longestPathStartFromRootSum(root)
        return self.maxPathSum_result

    def longestPathStartFromRootSum(self, root):
        if root:
            left_result = self.longestPathStartFromRootSum(root.left)
            right_result = self.longestPathStartFromRootSum(root.right)
            result = max(
                [root.val, left_result+root.val, right_result+root.val])
            self.maxPathSum_result = max(
                [self.maxPathSum_result, result, left_result+root.val+right_result])
            return result
        else:
            return -math.inf
