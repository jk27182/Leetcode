from __future__ import annotations

number_mapping = {
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': list('ghi'),
    '5': list('jkl'),
    '6': list('mno'),
    '7': list('pqrs'),
    '8': list('tuv'),
    '9': list('wxzy'),
    '0': [' '],
}
# build a tree from the given number Inputs and then use DFS to obtain solutions
from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class TreeNode():
    value: str
    left: Union[Optional[TreeNode], None] = None
    right: Union[Optional[TreeNode], None] = None


input_test = '23'

root = TreeNode('')
for number in input_test:
    chars = number_mapping[number]
    nodes = TreeNode(chars[0])
    for char in chars[1:]:
        pass
