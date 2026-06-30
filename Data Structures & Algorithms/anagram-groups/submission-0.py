from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #if the letter count and letters of the words are the same group them,
        #if they are different, put them in a different group
        #use a dict
        #use method where you alphabetically sort it
        
        seen = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            seen[key].append(i)
        return list(seen.values())
        


        