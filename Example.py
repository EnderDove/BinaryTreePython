"""importing BinaryTree module"""
import binary_tree as BT

if __name__ == '__main__':
    tree = BT.Tree(4, 2, 3, 1, 6, 5)
    tree.add_value(7)

    tree.display_tree()
    print(tree.find_value(7).path)
    print(tree.find_path('Right', 'Left').value)
    print(tree.min_node().value)
    del tree
