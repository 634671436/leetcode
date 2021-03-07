#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        # 在trie中作为最后一个字符的key存在，用于判断是否有结尾
        self.end = -1   


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curNode = self.root
        for c in word:
            if c not in curNode:
                curNode[c] = {}
            curNode =  curNode[c]
        curNode[self.end] = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for c in word:
            if c not in curNode:
                return False
            curNode = curNode[c]
        
        if self.end not in curNode:
            return False
        
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for c in prefix:
            if c not in curNode:
                return False
            curNode = curNode[c]
        
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

