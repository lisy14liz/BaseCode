import math
import functools

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0]*(2*self.n)

        for i in range(self.n):
            j = self.idx2tree_idx(i)
            self.tree[j] = nums[i]

        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i]+self.tree[2*i+1]

    def idx2tree_idx(self, pos):
        return pos + self.n

    def tree_idx2idx(self, idx):
        return idx - self.n

    def _update_parents(self, pos):
        while pos > 0:
            (left, right) = (pos, pos+1) if pos % 2 == 0 else (pos-1, pos)
            self.tree[pos//2] = self.tree[left] + self.tree[right]
            pos //= 2
    
    def update(self, pos, val):  # nums[pos]=val
        pos = self.idx2tree_idx(pos)
        self.tree[pos] = val
        self._update_parents(pos)

    def increase(self, pos, val=1):  # nums[pos]+=val
        pos = self.idx2tree_idx(pos)
        self.tree[pos] += val
        self._update_parents(pos)

    def sum_range(self, l, r):  # get the sum of nums[i:j+1]
        l, r = self.idx2tree_idx(l), self.idx2tree_idx(r)
        return self._sum_range_tree_idx_input(l, r)

    def _sum_range_tree_idx_input(self, l, r):
        res = 0
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res


class OrderedLeavesSegmentTree(SegmentTree):
    def __init__(self, nums):
        self.n = len(nums)
        self.height = ceil(math.log(2*self.n, 2))
        self.lowest_first_node = int(pow(2, self.height-1))
        super().__init__(nums)
        self.left = [0]*(2*self.n)
        self.right = [0]*(2*self.n)
        for i in range(self.n):
            j = self.idx2tree_idx(i)
            self.left[j] = i
            self.right[j] = i

        for i in range(self.n-1, 0, -1):
            self.left[i] = self.left[2*i]
            self.right[i] = self.right[2*i+1]

    def idx2tree_idx(self, pos):
        # [0,n-1] -> [n,2*n-1]:
        # [0,2*n-self.lowest_first_node-1] + [2*n-self.lowest_first_node,n-1] -> [lowest_first_node,2*n-1] + [n,lowest_first_node-1]
        if pos < 2*self.n-self.lowest_first_node:
            return pos+self.lowest_first_node
        else:
            return pos-self.n+self.lowest_first_node

    def tree_idx2idx(self, idx):
        if idx >= self.lowest_first_node:
            return idx - self.lowest_first_node
        else:
            return idx + self.n - self.lowest_first_node

    def sum_range(self, l, r):
        l, r = self.idx2tree_idx(l), self.idx2tree_idx(r)
        if r < self.lowest_first_node and l >= self.lowest_first_node:
            return self._sum_range_tree_idx_input(l, 2*self.n-1)+self._sum_range_tree_idx_input(self.n, r)
        return self._sum_range_tree_idx_input(l, r)