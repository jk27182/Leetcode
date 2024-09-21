from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Union

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# [3,1,4,3,null,1,5]
node5 = Node(5)
node1 = Node(1)
node3 = Node(3)
node4 = Node(4, node5, node1)
node11 = Node(1, node3)
root = Node(3, node11, node4)

def bfs(node):
    res = []
    if node is None:
        return []
    queue = [node]
    while len(queue) != 0:
        node = queue.pop(0)
        if not node:
            continue
        res.append(node.value)
        queue.append(node.left)
        queue.append(node.right)
    return res


print(bfs(root))