import copy

class Node:
    def __init__(self, data, next):
        self.__data = data
        self.__next = next

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_next(self, next):
        self.__next.append(next)

    def pop_next(self, next):
        self.__next.remove(next)

    def get_next(self):
        return self.__next

    def next_is_none(self):
        self.__next = None


def path(root: Node):
    cursor = root
    while curosr:
        pass

def path_helper(root, head, path_list, all_path_list=[]):
    if root.get_next() == None:
        all_path_list.append(copy.deepcopy(path_list))
        return
    path_list.append(root.get_data())
    for son in root.get_next():
        path_helper(son, head, path_list, all_path_list)
    if root == head:
        return all_path_list
    return

# def ichsheho()