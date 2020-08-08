import heapq


class myHeap:
    def __init__(self, data=None, max_length=None, heap_type='min', is_tuple=False):
        self.max_length = max_length
        self.heap_type = heap_type
        self.is_tuple = is_tuple
        if data is None:
            self.data = []
        else:
            if self.heap_type == 'max':
                data = [self._get_oppsite(d) for d in data]
            self.data = data
            heapq.heapify(self.data)

    def _get_oppsite(self, element):
        if self.is_tuple:
            return (-element[0],)+element[1:]
        else:
            return -element

    def _keep_size(self):
        poped = []
        if self.max_length is not None:
            while len(self.data) > self.max_length:
                poped.append(heapq.heappop(self.data))
        return poped

    def push(self, value):
        if self.heap_type == 'max':
            value = self._get_oppsite(value)
        heapq.heappush(self.data, value)
        poped = self._keep_size()
        return poped

    def pop(self):
        value = heapq.heappop(self.data)
        if self.heap_type == 'max':
            value = self._get_oppsite(value)
        return value

    def __getitem__(self, idx):
        value = self.data[idx]
        if self.heap_type == 'max':
            value = self._get_oppsite(value)
        return value

    def get_data(self):
        return [self._get_oppsite(d) for d in self.data] if self.heap_type == 'max' else self.data

    def length(self):
        return len(self.data)
