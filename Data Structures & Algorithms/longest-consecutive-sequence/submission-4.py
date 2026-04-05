class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res

'''
- Given an array of integers nums
- We want to return the length of the longest consecutive sequence of
  elements that can be formed
- Consecutive sequence: sequence of elements in which each element is
  exactly 1 greater than the previous element
    - The elements DO NOT have to be consecutive in the original array
- Algorithm must run in O(n) time

Ex. nums = [2, 20, 4, 10, 3, 4, 5]
    output = 4
    Explanation: the longest consecutive sequence is [2, 3, 4, 5]

Ex. nums = [0, 3, 2, 5, 4, 6, 1, 1]
    output = 7

My thought process:
    1. Sort array but that would be O(nlogn) most likely
    
    2. Use hashmap for each element in the array as the minimum and iterate
       array and count how many times hits of one greater there are

       key=nums : value=count
       2  : 1 + 3
       20 : 1 + 0
       4  : 1 + 1
       10 : 1 + 0
       3  : 1 + 2
       4  : 1 + 1
       5  : 1 + 0

Solution:
    1. Brute Force
       - Algorithm:
         1. Convert the input list toa set for O(1) lookups
         2. Initialize res to store the maximum streak length
         3. For each number num in the original list:
            - Start a new streak count at 0
            - Set curr = num
            - While curr exists in the set:
                - Increase the streak count
                - Move to the next number curr += 1
            - Update res with the longest streak foud so far
         4. Return res after checking all numbers
     
       - Code: 
         res = 0
         num_set = set(nums)

         for num in nums:
            streak = 0
            curr = num
            
            while curr in num_set:
                streak += 1
                curr += 1
            
            res = max(res, streak)

         return res

        Time: O(n^2)
        Space: O(n)

    2. Sorting
        - Algorithm:
            1. If the input list is empty, return 0
            2. Sort the array in non-decreasing order
            3. Initialize:
                - res to track the longest streak
                - curr as the first number
                - streak as 0
                - index i = 0
            4. While i is within bounds:
                - if nums[i] does not match curr, reset:
                    - curr = nums[i]
                    - streak = 0
                - Skip over all duplicates of curr by advancing i while
                  nums[i] == curr
                - Increase streak by 1 since we found the expected number
                - Increase curr by 1 to expect the next number in the sequence
                - Update res with the maximum streak found so far
            5. Return res after scanning the entire list

        - Code: 
            if not nums:
                return 0
            
            res = 0
            nums.sort()

            curr = nums[0]
            streak = 0
            
            i = 0
            while i < len(nums):
                if curr != nums[i]:
                    curr = nums[i]
                    streak = 0
                while i < len(nums) and nums[i] == curr:
                    i += 1
                streak += 1
                curr += 1
                res = max(res, streak)
            
            return res
        
        Time: O(nlogn)
        Space: O(1) or O(n) depending on sorting algorithm

    3. Hash Set
        - To avoid repeatedly recounting the same sequences, we only want
          to start counting when we find the beginning of a consecutive sequence
        - A number is the start of a sequence if num - 1 is not in the set
        - This guarantees that each consecutive sequence is counted exactly once
        - Once we idenitfy such a starting number, we simply keep checking if
          num + 1, num + 2, ... exist in the set and extend the streak as far as possible
        - This makes the solution efficient and clean because each number contributes
          to the sequence only one time
        
        - Algorithm:
            1. Convert the list into a set numSet for O(1) lookups
            2. Initialize longest to track the length of the longest
               consecutive sequence
            3. For each num in numSet:
                - Check if num - 1 is NOT in the set:
                    - If true, num is the start of the sequence
                    - Initialize length = 1
                    - While num + length exists in the set, increase length
                - Update longest witht he maximum length found
            4. Return longest after scanning all numbers

        - Code:
            numSet = set(nums)
            longest = 0

            for num in numSet:
                if (num - 1) not in numSet:
                    length = 1
                    while (num + length) in numSet:
                        length += 1
                    longest = max(length, longest)
            
            return 
        
        Time: O(n)
        Space: O(n)

    4. Hash Map
        - When we place a new number into the map, it may connect two
          existing sequences or extend one of them
        - Instead of scanning forward or backward, we only look at the lengths
          stored at the neighbors
            - mp[num-1] gives the length of the sequence ending right before num
            - mp[num+1] gives the length of the sequence starting right after num
        - By adding these together and including the current number, we know the
          total length of the new merged sequence
        - We then update the left boundary and right boundary of this sequence so the
          correct length can be retrieved later
        - This keeps the whole operation very efficient and avoids repeated work

        - Algorithm:
            1. Create a hashmap mp that stores sequence lengths at boundary positions
            2. Initialize res = 0 to store the longest sequence found
            3. For each number num in the input:
                - If num is already in mp, skip it
                - Compute the new sequence length:
                    - length = mp[num-1] + mp[num+1] + 1
                - Store this length at num
                - Update the boundaries:
                    - Left boundary: mp[num - mp[num-1]] = length
                    - Right boundary: mp[num + mp[num+1]] = length
                - Update res to keep track of the longest sequence
            4. Return res after processing all numbers
        
        Time: O(n)
        Space: O(n)

        - Code:
            mp = defaultdict(int)
            res = 0

            for num in nums:
                if not mp[num]:
                    mp[num] = mp[num - 1] + mp[num + 1] + 1
                    mp[num - mp[num-1]] = mp[num]
                    mp[num + mp[num+1]] = mp[num]
                    res = max(res, mp[num])
            
            return res
    

        [100, 4, 200, 1, 3, 2]
        
        mp = {key=num : value=0}
        res = 0
        
        mp[100] = mp[99] + mp[101] + 1 = 0 + 0 + 1 = 1
        mp[100 - mp[99]] = mp[100] -> mp[100] = 1
        mp[100 + mp[101]] = mp[100] -> mp[100] = 1
        res = 1

        mp[4] = mp[3] + mp[5] + 1 = 0 + 0 + 1 = 1
        mp[4 - mp[3]] = mp[4] -> mp[4] = 1
        mp[4 + mp[5]] = mp[4] -> mp[4] = 1
        res = 1

        mp[200] = mp[199] + mp[201] + 1 = 0 + 0 + 1 = 1
        mp[200 - mp[199]] = mp[200] -> mp[200] = 1
        mp[200 + mp[201]] = mp[200] -> mp[200] = 1
        res = 1

        mp[1] = mp[0] + mp[2] = 0 + 0 + 1 = 1
        mp[1 - mp[0]] = mp[1] -> mp[1] = 1
        mp[1 + mp[2]] = mp[1] -> mp[1] = 1
        res = 1

        mp[3] = mp[2] + mp[4] = 0 + 1 + 1 = 2
        mp[3 - mp[2]] = mp[3] -> mp[3] = 2
        mp[3 + mp[4]] = mp[3] -> mp[3 + 1] = mp[3] -> mp[4] = 2
        res = 2

        mp[2] = mp[1] + mp[3] = 1 + 2 + 1 = 4
        mp[2 - mp[1]] = mp[2] -> mp[2-1] = mp[2] -> mp[1] = 4
        mp[2 + mp[3]] = mp[2] -> mp[2+2] = mp[2] -> mp[4] = 4
        res = 4

'''
        