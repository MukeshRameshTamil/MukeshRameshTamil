class Solution(object):
    def groupAnagrams(self, strs):
      
        a=defaultdict(list)
        for word in strs:
            s=''.join(sorted(word))
            a[s].append(word)
        return list(a.values())
