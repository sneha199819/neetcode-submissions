class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        tt = list(t)
        for i in s:
            if i in tt:
                ss.remove(i)
                tt.remove(i)
            
        if len(ss)==0 and len(tt)==0:
            return True
        else:
            return False


s = 'jar'
t = 'jam'

ss = Solution()
ss.isAnagram(s,t)
