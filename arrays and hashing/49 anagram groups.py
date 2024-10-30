class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each word
        # count number of every letter
        # store in a hashmap letter count and list of words that have this letter counter
        # Key : 1e, 1a, 1t  Value : [eat, tea]
        # return all values of hashmap

        res = defaultdict(list) # automatically create list as default value for new keys
        #res = {} would throw a "Key error"

        for s in strs:
            count = [0] * 26 # a-z counts

            for c in s:
                count[ord(c)-ord("a")] +=1 #increase value at index 0 for a, 25 for z

            res[tuple(count)].append(s) #create new entry in hashmap if no word has same couts
                                # lists cannot be keys, so we convert list to tupe
                                # tuples are non mutable, lists are

        return res.values()