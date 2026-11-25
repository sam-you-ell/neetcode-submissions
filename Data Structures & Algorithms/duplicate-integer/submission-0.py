class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict(zip(nums, range(len(nums))))
        return len(d.keys()) != len(nums)


    #turn num into dictionary 
    # compare num of elements between dict and num. 
    # if no. of elements are not equal then has duplicate returns true?
