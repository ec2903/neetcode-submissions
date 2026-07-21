class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "" #create a new string first
        for i in s: 
            if i.isalnum():#checks whether the string contains only letter and numbers
                newStr += i.lower()
        else:
            return newStr == newStr[::-1]
        