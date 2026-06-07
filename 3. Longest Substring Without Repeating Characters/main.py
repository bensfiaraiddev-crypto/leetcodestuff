







class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        top_l : int = 0
        target : dict = {}
        a:int = 0
        while a<len(s) or s == "":
            letter = s[a]
            if letter in target:
                l = len(target)
                top_l = l if l>top_l else top_l
                print(top_l)
                s = s[target[letter]:]
                target = {}
                a = 0
            else:
                a += 1
                target[letter] =a
        top_l = len(target) if len(target)>top_l else top_l
        return top_l

            
   
print(Solution().lengthOfLongestSubstring(input()))            
