#Made by Chatgpt 
# Tree Traversal: Preorder, Inorder, Postorder, and Level Order

Tree traversal refers to the process of visiting all nodes of a tree in a systematic way. There are four main types of tree traversal techniques:

1. **Preorder Traversal (Depth-First)**
2. **Inorder Traversal (Depth-First)**
3. **Postorder Traversal (Depth-First)**
4. **Level Order Traversal (Breadth-First)**

---

## 1. Preorder Traversal (Root → Left → Right)

In Preorder Traversal, the root node is visited first, followed by the left subtree, and then the right subtree.

### Steps:
1. Visit the root node.
2. Traverse the left subtree.
3. Traverse the right subtree.

### Recursive Implementation
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root is None:
        return
    print(root.val, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)

# Example Usage
tree = TreeNode(1, TreeNode(2), TreeNode(3))
preorder_traversal(tree)
```
**Output:** `1 2 3`

### Iterative Implementation
```python
def preorder_traversal_iterative(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## 2. Inorder Traversal (Left → Root → Right)

In Inorder Traversal, the left subtree is visited first, followed by the root node, and then the right subtree.

### Steps:
1. Traverse the left subtree.
2. Visit the root node.
3. Traverse the right subtree.

### Recursive Implementation
```python
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=' ')
    inorder_traversal(root.right)
```
**Output:** `2 1 3`

### Iterative Implementation
```python
def inorder_traversal_iterative(root):
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val, end=' ')
        current = current.right
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## 3. Postorder Traversal (Left → Right → Root)

In Postorder Traversal, the left subtree is visited first, followed by the right subtree, and finally the root node.

### Steps:
1. Traverse the left subtree.
2. Traverse the right subtree.
3. Visit the root node.

### Recursive Implementation
```python
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val, end=' ')
```
**Output:** `2 3 1`

### Iterative Implementation
```python
def postorder_traversal_iterative(root):
    if root is None:
        return
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().val, end=' ')
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## 4. Level Order Traversal (Breadth-First Traversal)

In Level Order Traversal, nodes are visited level by level from top to bottom, and left to right at each level.

### Steps:
1. Start at the root node.
2. Use a queue to visit nodes level by level.

### Implementation
```python
from collections import deque

def level_order_traversal(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```
**Output:** `1 2 3`

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## Comparison Table
| Traversal Type  | Order         | Use Cases               |
|------------------|---------------|--------------------------|
| Preorder        | Root → Left → Right | Copying a tree structure |
| Inorder         | Left → Root → Right | Sorting binary search trees |
| Postorder       | Left → Right → Root | Deleting a tree          |
| Level Order     | Level by Level | Shortest path in a tree  |

---

## Conclusion
Understanding these traversal techniques is essential for solving tree-related problems in data structures and algorithms. Each traversal serves a specific purpose and has its own advantages depending on the use case.
