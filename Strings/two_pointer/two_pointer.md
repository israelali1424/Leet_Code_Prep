# Two-Pointer Approach

The **two-pointer approach** is a technique commonly used to solve problems involving arrays or linked lists. It utilizes two pointers (or indices) to traverse a data structure, often optimizing time complexity by reducing the need for nested loops.

## When to Use the Two-Pointer Approach
You can apply the two-pointer technique when:  
- You need to **find pairs** or **subarrays** in a sorted or unsorted array.  
- The problem involves **searching for elements** that satisfy certain conditions (e.g., sum, difference).  
- You want to **reduce the problem from O(n²) to O(n)** by eliminating nested loops.

---

## Types of Two-Pointer Approaches

### 1. **Opposite Direction Movement**
- One pointer starts from the **beginning** of the array, and the other starts from the **end**.  
- Both pointers move towards each other until the desired result is found.

#### Example Use Cases:
- Finding a pair of numbers that sum to a target in a sorted array.  
- Checking if an array is a palindrome.

---

### 2. **Same Direction Movement**
- Both pointers start from the **beginning** or **end** of the array and move at different speeds.  

#### Example Use Cases:
- Binary search Questions( given an array in ascending order)
- Detecting a cycle in a linked list (fast and slow pointers).  
- Finding the middle of a linked list.  
- Sliding window problems where one pointer expands the window, and the other shrinks it.

#Algos
Binary Seach is a common algo used  
---
## Notes
These notes were created using a combination of insights from ChatGPT and the YouTube video [Two Pointers Technique Explained by GeeksforGeeks](https://www.youtube.com/watch?v=ymKrGndnTis).
