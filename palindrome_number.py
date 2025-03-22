class Solution(object):
    def isPalindrome(self, x):
        if x>0:
            reverse = int(str(x)[::-1])
            if reverse == x:
                return True
            return False
        else:
            return False

        
