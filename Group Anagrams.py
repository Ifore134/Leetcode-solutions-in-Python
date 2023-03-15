class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       ans =[]
       for i in strs:
           d= {}
           for j in i:
               if j not in d:
                   d[j]=1
               else:
                  d[j]+=1
           if [d] not in ans:
               ans.append([d])
           
        
       for i in strs:
           d= {}
           for j in i:
               if j not in d:
                   d[j]=1
               else:
                  d[j]+=1
           for c in range(len(ans)):
               if d == ans[c][0]:
                   ans[c].append(i)
       for i in ans:
           i.remove(i[0])
       return ans
