def is_match(l, r):
    if not l or not r:
        return l == r
    return l.val == r.val and is_match(l.left, r.left) and is_match(l.right, r.right)