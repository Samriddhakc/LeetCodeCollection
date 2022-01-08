
"""
1166. Design File System.
You are asked to design a file system that allows you to create new paths and associate them with different values.
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.
Implement the FileSystem class:
bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
"""

from collections import defaultdict


class TrieNode:
    def __init__(self, name):
        self.name = name
        self.map = defaultdict(TrieNode)
        self.val = -1


class FileSystem:

    def __init__(self):

        self.root = TrieNode("")

    def createPath(self, path: str, value: int) -> bool:

        # all comp that will form a path
        components = path.split("/")

        # iterator for the root node
        curr = self.root

        # Iterate over all components
        for i in range(1, len(components)):
            name = components[i]

            if name not in curr.map:

                if i == (len(components) - 1):  # if it doesn't add it to the trie
                    curr.map[name] = TrieNode(name)
                else:
                    return False
            curr = curr.map[name]

        # If -1, then it is already populated.
        if curr.val != -1:
            return False

        curr.val = value
        return True

    def get(self, path: str) -> int:

        curr = self.root
        components = path.split("/")

        for i in range(1, len(components)):
            name = components[i]
            if name not in curr.map:
                return -1
            curr = curr.map[name]

        return curr.val
