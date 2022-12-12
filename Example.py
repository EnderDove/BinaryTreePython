import BinaryTree as BT

tree = BT.Tree(4, 2, 3, 1, 6, 5)
tree.addValue(7)

tree.displayTree()
print(tree.findValue(7).path)
print(tree.findPath('Right', 'Left').value)

del tree
