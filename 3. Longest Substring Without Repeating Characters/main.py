







class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_lenght : int = 0
        left = 0
        for right in range(len(s)):
            print(char_set)
            if s[right] in char_set:
                char_set.remove(s[right])
                left +=1

            char_set.add(s[right])
            max_lenght = max(max_lenght,right - left +1)
        return max_lenght


print(Solution().lengthOfLongestSubstring(input()))
