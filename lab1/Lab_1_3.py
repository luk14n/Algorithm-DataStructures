from Tree import Tree
from BTS import BTS
arr = ['a', 'b', 'c', 'd', 'e', 'f']
a = Tree(n=6, data=arr)
a.ShowTree(root=a.root)
s = '87 71 81 84 73 66 77 87 71 73 92 75 61'
s = [int(i) for i in s.split(' ')]
s.sort()
print(s)
