class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a =0
        count=0
        for i in range(len(s)):
            sub =[]
            c=0
            for j in range(i,len(s)):
                if s[j] in sub:
                    break
                sub.append(s[j])
                c+=1
            if c>count:
                count=c
        return count
