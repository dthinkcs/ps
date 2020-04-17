
class TrieNode:

    def __init__(self, isWord = False):
        self.isWord = isWord
        self.hm = dict()

    def insertWord(self, word):
        if len(word) == 0:
            self.isWord = True
            return
        if word[0] not in self.hm:
            self.hm[word[0]] = TrieNode()
        self.hm[word[0]].insertWord(word[1:])

    def checkWord(self, word):
        if len(word) == 0:
            return self.isWord
        if word[0] not in self.hm:
            return False
        return self.hm[word[0]].checkWord(word[1:])

    def getTrieNode(self, letter):
        if len(letter) == 0:
            return self
        return self.hm.get(letter, None)

a = TrieNode()
a.insertWord('mama')
val = a.getTrieNode('m')

print(val)

val = val.getTrieNode('a')

print(val)s
