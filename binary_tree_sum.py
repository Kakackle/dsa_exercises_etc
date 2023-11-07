class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    # def __str__(self):
        # ret = '[Root] ' + str(self.val)
        # base = self.val
        # left = base.left
        # right = base.right
        # while left or right:
        #     if left:
        #         ret += str(left.val)
        #         left = left.left
        #     if right:
        #         ret += str(right.right)

# class Tree:
#     def __init__(self, left, right)

root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(6)

def sum_tree(node):
    # if node.left:
    #     return node.val + sum_tree(node.left)
    # if node.right:
    #     return node.val + sum_tree(node.right)
    # else:
    #     return node.val

    if node.left or node.right:
        return node.val + sum_tree(node.left) + sum_tree(node.right)
    else:
        return node.val

    # if node == None:
    #     return 0
    # return node.val + sum_tree(node.left) + sum_tree(node.right)

print(sum_tree(root))