
"""
this file contians the Node object and a dict containing the possible movements on the board
"""

MOVES_DICT = {"Up": (0, 1), "Down": (0, -1), "Right": (1, 0), "Left": (-1, 0)}


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
