class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        while i < len(nums):
            j,product = 0,1 
            while j < len(nums):
                if i != j:
                    product *= nums[j]
                j+=1
            output.append(product)
            i+=1
        return output