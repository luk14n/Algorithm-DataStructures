INDENTATON = 3


class Node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class BTS:
    def __init__(self):
        self.root = None

    def CreateBTS(self, data):
        self.root = Node(data=data)

    def _SearchNodeBST(self, data, root: Node):
        if root is None:
            return None
        if root.data == data:
            return root
        if root.data > data:
            return self._SearchNodeBST(data=data, root=root.left)
        else:
            return self._SearchNodeBST(data=data, root=root.right)

    def SearchNodeBST(self, data):
        return self._SearchNodeBST(data=data, root=self.root)

    def _ShowTree(self, root: Node, indent: int = 0):
        if root is None:
            return
        indent += INDENTATON
        self._ShowTree(root.right, indent=indent)
        print()
        for i in range(INDENTATON, indent):
            print(end=" ")
        print(root.data)
        self._ShowTree(root.left, indent=indent)

    def ShowTree(self, indent: int = 0):
        print('-'*20)
        self._ShowTree(root=self.root, indent=indent)
        print('-'*20)

    def InsertNodeBST(self, data):
        if self.SearchNodeBST(data=data) is not None:
            return False
        self._InsertNode(data=data)
        return True

    def _InsertNode(self, data):
        prev_node = None
        node: Node = self.root
        while node is not None:
            if node.data > data:
                prev_node = node
                node = node.left
            else:
                prev_node = node
                node = node.right
        new_node = Node(data=data, parent=prev_node)
        if prev_node.data > data:
            prev_node.left = new_node
        elif prev_node.data < data:
            prev_node.right = new_node

    def DelNode(self, data):
        node: Node = self.SearchNodeBST(data=data)
        if node is None:
            return False
        if node.left is None and node.right is None:
            parent: Node = node.parent
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            del node
        elif node.left is None or node.right is None:
            parent: Node = node.parent
            if node.left is not None:
                child: Node = node.left
            elif node.right is not None:
                child: Node = node.right

            if parent.left == node:
                parent.left = child
            else:
                parent.right = child
            del node
        else:
            sucessor = self.SuccessorNodeBST(root=node)
            sucessor_data= sucessor.data
            self.DelNode(sucessor.data)
            node.data = sucessor_data

    def SuccessorNodeBST(self, root: Node):
        if root is None:
            return None
        if root.right is not None:
            return self._minimum(root=root.right)
        y: Node = root.parent
        while y is not None and root is y.right:
            root = y
            y = root.parent
        return y

    def PredecessorNodeBST(self, root: Node):
        if root is None:
            return None
        if root.left is not None:
            return self._maximum(root=root.left)
        y: Node = root.parent
        while y is not None and root is y.left:
            root = y
            y = root.parent
        return y

    @staticmethod
    def _minimum(root: Node):
        while root.left is not None:
            root = root.left
        return root

    @staticmethod
    def _maximum(root: Node):
        while root.right is not None:
            root = root.right
        return root
