import math
import functools


class SegmentTree:
    def __init__(self, nums, version='zkw'):
        # version can be in ['zkw', 'ordered_leaves']
        self.version = version
        if not nums:
            return
        n = len(nums)
        self.n = n
        self.tree = [0]*(2*n)
        if self.version != 'zkw':
            self.left = [0]*(2*n)
            self.right = [0]*(2*n)
            self.height = ceil(math.log(2*n, 2))
            self.lowest_first_node = int(pow(2, self.height-1))
        for i in range(n):
            j = self.idx2tree_idx(i)
            self.tree[j] = nums[i]
            if self.version != 'zkw':
                self.left[j] = i
                self.right[j] = i
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[2*i]+self.tree[2*i+1]
            if self.version != 'zkw':
                self.left[i] = self.left[2*i]
                self.right[i] = self.right[2*i+1]

    def idx2tree_idx(self, pos):
        # [0,n-1] -> [n,2*n-1]:
        # [0,2*n-self.lowest_first_node-1] + [2*n-self.lowest_first_node,n-1] -> [lowest_first_node,2*n-1] + [n,lowest_first_node-1]
        if self.version == 'zkw':
            return pos + self.n
        if pos < 2*self.n-self.lowest_first_node:
            return pos+self.lowest_first_node
        else:
            return pos-self.n+self.lowest_first_node

    def tree_idx2idx(self, idx):
        if self.version == 'zkw':
            return idx - self.n
        if idx >= self.lowest_first_node:
            return idx - self.lowest_first_node
        else:
            return idx + self.n - self.lowest_first_node

    def update(self, pos, val): # nums[pos]=val
        pos = self.idx2tree_idx(pos)
        self.tree[pos] = val
        while pos > 0:
            (left, right) = (pos, pos+1) if pos % 2 == 0 else (pos-1, pos)
            self.tree[pos//2] = self.tree[left] + self.tree[right]
            pos //= 2

    def sumRange(self, l, r, is_tree_idx=False): # get the sum from nums[i] to nums[j]
        if not is_tree_idx:
            l = self.idx2tree_idx(l)
            r = self.idx2tree_idx(r)
        if self.version != 'zkw' and r < self.lowest_first_node and l >= self.lowest_first_node:
            return self.sumRange(l, 2*self.n-1, True)+self.sumRange(self.n, r, True)
        res = 0
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l /= 2
            r /= 2
        return res
