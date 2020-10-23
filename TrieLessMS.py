# Kinda scummy imo, but it works the fastest. Doesn't seem optimized for memory.
# This script basically organises words by their length and finds them in the dictionary. Kinda weird.

import collections

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key: len; val: [list of words]
        self.d = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        n = len(word)
        self.d[n].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        n = len(word)
        if not self.d[n]:
            return False
        found = False
        for w in self.d[n]:
            if w == word:
                return True
            i = 0
            # Below is to accomodate for '.' wildcard letters
            while i < n:
                if w[i] == word[i] or word[i] == ".":
                    i += 1
                else:
                    break
            if i == n:
                found = True
        if found:
            return True

        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)





# self.index = {}
# self.memory = collections.defaultdict(set)


# def compare(self, w1: str, w2: str) -> bool:
#         n = len(w1)
#         i1, i2 = 0, 0
#         while i1 < n and i2 < n:
#             if w1[i1] == w2[i2] or w2[i2] == '.':
#                 i1 += 1
#                 i2 += 1
#             else:
#                 return False
#         return True


# self.index[word] = True
# self.memory[len(word)].add(word)


# if word in self.index:
#             return True

#         word_len = len(word)
#         if word_len not in self.memory:
#             return False

#         if word == '.' * word_len:
#             return True

#         words = self.memory[word_len]
#         for w in words:
#             if self.compare(w, word):
#                 return True

#         return False