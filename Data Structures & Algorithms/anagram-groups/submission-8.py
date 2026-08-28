class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list) #creating a hashmap to count the number of characters of each a-z in the string and store them

        for s in strs:
            count = [0] * 26 #26 characters from a to z

            for c in s: 
                #map A to index 0 Map Z to c is essentially the index number
                count[ord(c) - ord('a')] += 1
            results[tuple(count)].append(s)
        return list(results.values())


