from collections import defaultdict

class Trie():

    def __init__(self):
            """
            Initialize your data structure here.
            """
            self.root = defaultdict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for letter in word:
            cur = cur.setdefault(letter, {})

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        cur = self.root
        for letter in word:
            if letter not in cur:
                if letter == '.':
                    for i in cur.keys():
                        if self.search(word.replace('.', i, 1)) == True:
                            return True
                    return False
                else:
                    return False
            else:
                cur = cur[letter]
        return True

test = Trie()
test.addWord('at')
test.addWord('and')
test.addWord('an')
test.addWord('add')
print(test.search('a'))