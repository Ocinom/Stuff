from collections import defaultdict

class Trie():
    """
    Make trie with insert, search, startswith
    """

    def __init__(self):
        self.root = defaultdict()

    def insert(self, word):
        cur = self.root
        for letter in word:
            cur = cur.setdefault(letter, {})

    def search(self, word):
        cur = self.root
        for letter in word:
            print(cur.keys())
            if letter not in cur:
                return False
            cur = cur[letter]
        return True

    def startsWith(self, prefix):
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]
        return True

test = Trie()
test.insert('helloworld')
test.insert('ilikeapple')
test.insert('helloz')

print(test.search('hello'))
