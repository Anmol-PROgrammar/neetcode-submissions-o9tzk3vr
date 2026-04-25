class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the largest element
        # then check target is less or larger than largest element
        # target will exists in either half of the largest element.
        largest = max(nums);
        index_of_largest = nums.index(largest)

        if target == largest:
            return index_of_largest
        if target > largest:
            return -1

        n = len(nums)
        l, r = 0, n - 1

        if n - 1 == index_of_largest:
            l = 0
            r = index_of_largest
        elif target >= nums[0]  and target <= nums[index_of_largest]:
            l, r = 0, index_of_largest
        
        elif index_of_largest + 1 < n and target >= nums[index_of_largest + 1] and target <= nums[n-1] :
            l, r = index_of_largest + 1, n - 1 
        
        while l <= r:
            mid = l + (r - l) // 2;
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else: 
                l = mid + 1

        return -1