class Node:
    """Create a Node for Binary Tree
    
    Values:
        value (Any): Node Value
        distance (int): Distance from the root
        displacement (int): Horizontal displacement from the root
        path (list(str)): Path to the current node
        parent (Node): The Ancestor Node Object
        left (Node): The Object of the Left child Node
        right (Node): The Object of the Right child Node
        
    """
    def __init__(self, value, _parent: object | None = None, _path: list = []):
        self.value = value
        self.distance = len(_path)
        self.displacement = abs(_path.count('Right') - _path.count('Left'))
        self.path = _path
        self.parent = _parent
        self.left = None
        self.right = None


class Tree:
    """Create a Binary Tree
    
    Values:
        root (Node): The Tree Root Node Object
    
    Methods:
        addValue (value): Adding a new node to the tree
        findValue (value): Search for a Node Object in the Tree by Value query
        findPath (path): Search for a Node Object in the Tree by Path query
        displayTree (): Print Tree graphics
    """
    def __init__(self):
        self.root = None

    def addValue(self, value, _node: None | Node = None, _path: list = []) -> None:
        """Adding a new node to the tree

        Args:
            value (Any): New Node Value

        Possible exceptions:
            ValueError: Node values in the same tree must be of the same type
        """
        if self.root is None:
            self.root = Node(value, None, [])
            return

        if _node is None:
            _node = self.root
            _path = []

        if type(value) != type(_node.value):
            raise ValueError('Node values in the same tree must be of the same type')

        if value < _node.value:
            _path.append('Left')
            if _node.left is None:
                _node.left = Node(value, _node, _path)
            else:
                self.addValue(value, _node.left, _path)

        if value > _node.value:
            _path.append('Right')
            if _node.right is None:
                _node.right = Node(value, _node, _path)
            else:
                self.addValue(value, _node.right, _path)

    def findValue(self, value, _node: None | Node = None) -> Node:
        """Search for a Node Object in the Tree by Value query

        Args:
            value (Any): Requested Value

        Returns:
            Node: Node Object with requested Value
        """
        if _node is None:
            _node = self.root

        if self.root is None:
            return self.root

        if value == _node.value:
            return _node

        if (value < _node.value and _node.left is not None):
            return self.findValue(value, _node.left)

        if (value > _node.value and _node.right is not None):
            return self.findValue(value, _node.right)
        return self.root

    def findPath(self, *_path: str) -> Node:
        """Search for a Node Object in the Tree by Path query

        Args:
            path (tuple(str)): Requested Path

        Returns:
            Node: Node Object with requested Path
        """

        if _path is None:
            return self.root

        _node = self.root
        for i in _path:
            if i == 'Left':
                if _node.left is None:
                    return self.root
                _node = _node.left
            if i == 'Right':
                if _node.right is None:
                    return self.root
                _node = _node.right
        return _node

    def displayTree(self, _node: None | Node = None) -> None:
        """Print Tree graphics

        Prints:
            Tree terminal graphics
        """
        if _node is None:
            lines, *_ = self.displayTree(self.root)
            for line in lines:
                print(line)
            return
        
        if _node.right is None and _node.left is None:
            line = '%s' % _node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if _node.right is None:
            lines, n, p, x = self.displayTree(_node.left)
            s = '%s' % _node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if _node.left is None:
            lines, n, p, x = self.displayTree(_node.right)
            s = '%s' % _node.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        
        if _node.left is not None and _node.right is not None:
            left, n, p, x = self.displayTree(_node.left)
            right, m, q, y = self.displayTree(_node.right)
            s = '%s' % _node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * \
                '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + \
                (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif p > q:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
