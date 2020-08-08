from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.childs = defaultdict(TrieNode)
        self.isEnd = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            cur = cur.childs[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur.childs:
                return False
            cur = cur.childs[c]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            if c not in cur.childs:
                return False
            cur = cur.childs[c]
        return True


class WordDictionary(Trie):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        super().__init__()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        super().insert(word)

    def search_variant1(self, word: str, node=None):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if node is None:
            node = self.root
        if not word:
            if node.isEnd:
                return True
            else:
                return False
        else:
            if word[0] == '.':
                if not node.childs:
                    return False
                result = []
                for child in node.childs.values():
                    result.append(self.search_variant1(word[1:], child))
                return any(result)
            else:
                if word[0] in node.childs:
                    return self.search_variant1(word[1:], node.childs[word[0]])
                else:
                    return False
