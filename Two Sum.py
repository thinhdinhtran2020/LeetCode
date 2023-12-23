class Solution:
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            pointer1 = nums[x]
            for y in range(len(nums)):
                pointer2 = nums[y]
                if x == y:
                    pass
                else:
                    if (pointer1 + pointer2) == target:
                        return ([x,y])
                    
def main():
    sample = [2,7,11,15]
    solution = Solution()
    print (solution.twoSum(sample, 9))
    
main()
