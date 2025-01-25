'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
'''
# 1/23/2025 My Solution passed 13/16 test cases on leetcode
class Trie:

    def __init__(self):
        self.trie = [] 
        self.seen =  set()

    def insert(self, word: str) -> None:
        
        self.trie.append([word])
        if word not in self.seen:
            self.seen.add(word)

    def search(self, word: str) -> bool:
        if word in self.seen:
            return True
        else:
            return False 
        
    def startsWith(self, prefix: str) -> bool:
        prev = None 
        if len(self.trie) > 0:
            prev = self.trie[-1][0]

        if  not prev: 
            return False 
        if prev < prefix:
            return False 
        
        for letter in range(0,len(prefix)):
            if prefix[letter] != prev[letter]:
                return False 
        
        return True 

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
#chatgpt version 1
class Trie:
    def __init__(self):
        # Use a dictionary to store the trie structure
        self.root = {}
        # Keep track of complete words
        self.words = set()
    
    def insert(self, word: str) -> None:
        # Start at the root node
        node = self.root
        
        # Insert each character into the trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        
        # Mark the end of a word
        node['$'] = True
        self.words.add(word)
    
    def search(self, word: str) -> bool:
        # Check if the word exists in the set of words
        return word in self.words
    
    def startsWith(self, prefix: str) -> bool:
        # Traverse the trie to check if prefix exists
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Test Cases
if __name__ == "__main__":
    trie = Trie()
    
    # Test Case 1: Insert and search a word
    trie.insert("apple")
    result1 = trie.search("apple")
    print("Test Case 1:", result1, "Passed" if result1 == True else "Failed")
    assert result1 == True
    # Expected Output: True

    # Test Case 2: Search for a word that does not exist
    result2 = trie.search("app")
    print("Test Case 2:", result2, "Passed" if result2 == False else "Failed")
    assert result2 == False
    # Expected Output: False

    # Test Case 3: Check if a prefix exists
    result3 = trie.startsWith("app")
    print("Test Case 3:", result3, "Passed" if result3 == True else "Failed")
    assert result3 == True
    # Expected Output: True

    # Test Case 4: Insert a prefix and search for it
    trie.insert("app")
    result4 = trie.search("app")
    print("Test Case 4:", result4, "Passed" if result4 == True else "Failed")
    assert result4 == True
    # Expected Output: True