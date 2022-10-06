
class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next = n
    def get_next(self):
        return self.next
    def set_next(self):
        self.next = n
    def get_data(self):
        return self.data
    def set_data(self):
        self.data = d

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0