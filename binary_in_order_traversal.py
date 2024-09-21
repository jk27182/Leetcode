self.res = []

def helper(node):
    if not node:
        return
    self.res.append(node.val)
    

def traverse(node):
    if not node:
        return
    traverse(node.left)
    helper(node) 
    traverse(node.right)

traverse(root)
return self.res