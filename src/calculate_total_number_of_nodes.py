class Node:
    def get_left_child(self):
        pass

    def get_right_child(self):
        pass


def calculate_total_number_of_nodes(root):
    ld = left_depth(root)
    rd = right_depth(root)
    if ld == rd:
        return 2 ** ld - 1
    return (1 + calculate_total_number_of_nodes(root.left)
            + calculate_total_number_of_nodes(root.right))


def left_depth(root):
    depth = 0
    while root is not None:
        root = root.left
        depth += 1
    return depth


def right_depth(root):
    depth = 0
    while root is not None:
        root = root.right
        depth += 1
    return depth
