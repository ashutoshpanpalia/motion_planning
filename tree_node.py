class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __repr__(self):
        return f"X= {self.x}, Y= {self.y}, Parent = {self.parent}"
        