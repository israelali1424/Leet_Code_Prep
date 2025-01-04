# Linked List Refresher

## 📚 **What is a Linked List?**
A **Linked List** is a linear data structure where elements, called **nodes**, are linked together using pointers.

Each node contains:
- **Data:** The value stored in the node.
- **Pointer (Next):** A reference to the next node in the sequence.

### 🧠 **Key Characteristics:**
- Dynamic size (can grow/shrink during runtime).
- Efficient insertions and deletions compared to arrays.
- Sequential access (no direct indexing).

---

## 🛠️ **Types of Linked Lists**
1. **Singly Linked List:** Nodes point only to the next node.
2. **Doubly Linked List:** Nodes point to both previous and next nodes.
3. **Circular Linked List:** The last node points back to the first node.

---

## 🔗 **Basic Operations**

### 1. **Traversal**
- Visit each node in the list.
```python
current = head
while current:
    print(current.data)
    current = current.next
```

### 2. **Insertion**
- **At the beginning:** Update `head` to the new node.
- **At the end:** Traverse to the last node and update `next`.
- **At a specific position:** Adjust pointers.

### 3. **Deletion**
- **From the beginning:** Update `head`.
- **From the end:** Traverse to the second-last node and set `next` to `None`.
- **At a specific position:** Adjust pointers to skip the node.

---

## 🚀 **Common Problems**
1. Detecting a cycle in a linked list (Floyd's Cycle Detection Algorithm).
2. Finding the middle of a linked list.
3. Reversing a linked list.
4. Merging two sorted linked lists.

### Example: **Reverse a Linked List**
```python
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

---

## 📝 **Big O Notation**
- **Access:** O(n)
- **Search:** O(n)
- **Insertion:** O(1) (if the pointer is already known)
- **Deletion:** O(1) (if the pointer is already known)

---

## 📖 **Use Cases**
- Implementing stacks and queues.
- Undo functionality in editors.
- Hash table chaining.

---

## 📊 **Comparison with Arrays**
| Feature          | Linked List | Array      |
|------------------|-------------|------------|
| Size            | Dynamic     | Fixed      |
| Insertion/Deletion | O(1)       | O(n)       |
| Access          | O(n)        | O(1)       |

---

## 🎯 **Tips for Interviews**
- Always clarify if it's singly, doubly, or circular linked list.
- Be familiar with edge cases (empty list, one node, cycles).
- Practice pointer manipulation (e.g., `prev`, `current`, `next`).

