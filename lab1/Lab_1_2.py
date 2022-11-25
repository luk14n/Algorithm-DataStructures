INDENTATON = 6


class Node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class Tree:
    def __init__(self, n: int, data=None):
        if isinstance(data, list):
            self.arr = data
            self.index = 0
            self._ChangeData(n=n, data=data)
            self.root = Node(data=self.data)
            self._ChangeData(n=n-1, data=self.arr)

            self.CreateTree(n=n // 2, parent=self.root, data=self.arr)
            self.CreateTree(n=n - n // 2 - 1, parent=self.root, data=self.arr)
        else:
            self.data = n
            self.root = Node(data=self.data)
            self._ChangeData(n=n, data=self.data)
            self.CreateTree(n=n // 2, parent=self.root, data=self.data)
            self.CreateTree(n=n - n // 2, parent=self.root, data=self.data)

    def _ChangeData(self, n, data):
        if isinstance(data, int):
            self.data = self.data - 1
        elif isinstance(data, list):
            try:
                self.data = self.arr[self.index]
            except IndexError:
                return None
            else:
                self.index += 1
        # print(self.data, end=' -!-')

    def CreateTree(self, n: int, parent: Node, data):
        if n == 0:
            return None
        else:
            new_node = Node(data=self.data, parent=parent)
            if parent.left is None:
                parent.left = new_node
            else:
                parent.right = new_node
            self._ChangeData(n=n, data=data)
            self.CreateTree(n=n // 2, parent=new_node, data=data)
            self.CreateTree(n=n - n // 2 - 1, parent=new_node, data=data)

    def Depth(self, root: Node):
        if root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return self.Depth(root=root.right) + 1
        elif root.right is None:
            return self.Depth(root=root.left) + 1
        else:
            return max(self.Depth(root=root.left), self.Depth(root=root.right)) + 1

    def InOrderTraversal(self, root: Node):
        if root is None:
            return
        self.InOrderTraversal(root.left)
        print(root.data)
        self.InOrderTraversal(root.right)

    def PreOrderTraversal(self, root: Node):
        if root is None:
            return
        print(root.data)
        self.PreOrderTraversal(root.left)
        self.PreOrderTraversal(root.right)

    def PostOrderTraversal(self, root: Node):
        if root is None:
            return
        self.PostOrderTraversal(root.left)
        self.PostOrderTraversal(root.right)
        print(root.data)

    def ShowTree(self, root: Node, indent: int = 0):
        if root is None:
            return
        indent += INDENTATON
        self.ShowTree(root.right, indent=indent)
        print()
        for i in range(INDENTATON, indent):
            print(end=" ")
        print(root.data)
        self.ShowTree(root.left, indent=indent)
