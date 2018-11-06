class TrieNode:
	def __init__(self):
		self.children = {}
		self.is_word = False
		self.word = ""
class Trie:
	def __init__(self):
		self.root = TrieNode()
	def insert(self, word):
		temp = self.root
		for i in word:
			if i not in temp.children:
				temp.children[i] = TrieNode()
			temp=temp.children[i]
		temp.is_word=True
		temp.word=word
	def search(self, word):
		temp = self.root
		for i in word:
			if i not in temp.children:
				return False
			temp=temp.children[i]
		return temp.is_word
	def startsWith(self, prefix):
		temp = self.root
		for i in prefix:
			if i not in temp.children:
				return False
			temp=temp.children[i]
		return True
	def allPrefixStrings(self,prefix):
		temp=self.root
		for i in prefix:
			if i not in temp.children:
				return []
			temp=temp.children[i]
		store = []
		def getWords(temp):
			if not temp:
				return
			if temp.is_word:
				store.append(temp.word)
			for child in temp.children.values():
				getWords(child)
		getWords(temp)
		return store
strings = ['apple','apt','mont','alum','ap','a']
prefix = 'ap'
trie = Trie()
for s in strings:
	trie.insert(s)
print(trie.allPrefixStrings(prefix))
