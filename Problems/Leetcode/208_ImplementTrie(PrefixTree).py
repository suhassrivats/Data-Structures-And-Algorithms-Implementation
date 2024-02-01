class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    """
    basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


    print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
    print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
    print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))
    Is "a"   a word: True
    Is "ad"  a word: False
    Is "add" a word: True

    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        for c in prefix:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                return False
        return True
        # current_node = self.root
        # for char in prefix:
        #     current_node = current_node.children.get(char)
        #     if current_node is None:
        #         return False
        # return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


def test_trie():
    trie = Trie()

    # Insert some words
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("app")
    trie.insert("bat")
    trie.insert("ball")

    # Test search
    assert trie.search("apple") == True
    assert trie.search("banana") == True
    assert trie.search("app") == True
    assert trie.search("bat") == True
    assert trie.search("ball") == True
    assert trie.search("application") == False
    assert trie.search("b") == False

    # Test startsWith
    assert trie.startsWith("a") == True
    assert trie.startsWith("ap") == True
    assert trie.startsWith("ban") == True
    assert trie.startsWith("bat") == True
    assert trie.startsWith("bal") == True
    assert trie.startsWith("c") == False
    assert trie.startsWith("z") == False

    print("All test cases passed successfully!")


if __name__ == "__main__":
    test_trie()
