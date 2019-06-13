class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        i = len(self.storage) - 1
        self._bubble_up(i)

    def delete(self):
        if len(self.storage) == 0:
            return None
        if len(self.storage) == 1:
            return self.storage.pop()
        else:
            self.storage[0], self.storage[len(
                self.storage) - 1] = self.storage[len(self.storage)-1], self.storage[0]
            removed = self.storage.pop()
            self._sift_down(0)

        return removed

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        p = (index - 1) // 2
        if index <= 0:
            return
        elif self.storage[index] > self.storage[p]:
            self.storage[index], self.storage[p] = self.storage[p], self.storage[index]
            self._bubble_up(p)

    def _sift_down(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        max = index
        if len(self.storage) > left and self.storage[max] < self.storage[left]:
            max = left
        if len(self.storage) > right and self.storage[max] < self.storage[right]:
            max = right
        if max == index:
            return
        else:
            self.storage[index], self.storage[max] = self.storage[max], self.storage[index]
            self._sift_down(max)