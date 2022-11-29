class Node:
    def __or__(self, func):
        return func(self)
