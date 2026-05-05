def kthSmallestElement(k, root):
	stack = []
	while root or stack:
		while root:
			stack.append(root)
			root = root.left
		small = stack.pop()
		k -= 1
		if k == 0:
			return small.val
		root = small.right
