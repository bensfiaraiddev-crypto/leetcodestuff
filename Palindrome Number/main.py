from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        elements : List[int] = []
        while x > 0:
            n:float = x / 10.0
            x = x// 10
            elements.append((n-x)*10)
        return elements == elements[::-1]



        
