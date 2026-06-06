







class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        collction : list = []
        for index,letter in  enumerate(s):
            if not letter in  collction:
                collction.append(letter)
                
        return len(collction)
            
