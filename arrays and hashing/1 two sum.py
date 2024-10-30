class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        encountered={} # a hashmap that stores every int encountered along with their index
        for i, v in enumerate(nums): # for each int
            diff=target-v # calculate the missing int
            if diff in encountered: # if missing int was encountered before
                return[encountered[diff],i] # return index of current int and missing int
            encountered[v] = i # store the current int and its index