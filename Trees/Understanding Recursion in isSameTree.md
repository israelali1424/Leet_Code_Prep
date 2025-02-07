# Understanding Recursion in `isSameTree`

## **How Does This Function Work?**

Imagine you're exploring a big tree. You **always go to the leftmost branch first**, checking each node along the way. Once you hit a dead end (a `None` node), you **start coming back up** and then check the right side.

---

## **Step-by-Step Example**

Let's say we have these two trees:

```
    1
   / \
  2   3
```

### **What Happens in the Code?**

1. **Start at `1`** → Go **left** to `2`
2. **At `2`**, go **left** → `None` (returns `True` ✅)
3. **Back at `2`**, check value (`2 == 2`) ✅
4. **At `2`**, go **right** → `None` (returns `True` ✅)
5. **Back at `1`**, left side is **done** ✅
6. **At `1`**, check value (`1 == 1`) ✅
7. **At `1`**, go **right** to `3`
8. **At `3`**, go **left** → `None` (returns `True` ✅)
9. **Back at `3`**, check value (`3 == 3`) ✅
10. **At `3`**, go **right** → `None` (returns `True` ✅)
11. **Everything matches!** Return `True` 🎉

---

## **How the Function "Unwinds" Back Up**

Recursion is like stacking plates. The function **goes all the way down the left side first**, then **comes back up**, and finally checks the right side.

### **Call Stack Visualization**

```
dfs(1,1)
 ├── dfs(2,2)
 │    ├── dfs(None, None) ✅ (returns True)
 │    ├── Check value `2 == 2` ✅
 │    ├── dfs(None, None) ✅ (returns True)
 │    ├── Return True for dfs(2,2)
 ├── Check value `1 == 1` ✅
 ├── dfs(3,3)
 │    ├── dfs(None, None) ✅ (returns True)
 │    ├── Check value `3 == 3` ✅
 │    ├── dfs(None, None) ✅ (returns True)
 │    ├── Return True for dfs(3,3)
 ├── Return True for dfs(1,1)
```

---

## **Why Does Left Get Checked First?**

Because Python **executes function calls immediately**. When the function sees this line:

```python
left = dfs(p.left, q.left)
```

- It **pauses everything else** and goes **deep into the left subtree first**.
- It **only moves forward** once `dfs(p.left, q.left)` is completely finished.

It's like asking a parent:

- **Kid:** "Can I go outside?"
- **Parent:** "First, do your homework."
- **Kid:** *Pauses, does homework first before asking again.*

The "homework" here is `dfs(p.left, q.left)`, which **must finish before anything else** happens.

---

## **Optimizing the Code**

Right now, the function **always checks the left subtree first, even if the values are different**. We can **save time** by checking values **before** recursion:

```python
def dfs(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:  # Check mismatch first!
        return False
    return dfs(p.left, q.left) and dfs(p.right, q.right)
```

### **Why is this better?**
- If `p.val != q.val`, we **immediately return False** instead of wasting time checking left/right subtrees.
- **Faster execution**, especially for large trees! 🚀

---

## **Final Takeaway**
- The function **goes all the way to the leftmost node first**.
- It **comes back up**, checking values along the way.
- Then it **moves to the right subtree**.
- **By checking values first**, we can make it more efficient.

🔥 **Now you understand recursion like a pro!** 🎉😊

