class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        
        for s in strs:
            x = ''.join(sorted(s))
            a[x].append(s)
        
        return a.values()
    
        