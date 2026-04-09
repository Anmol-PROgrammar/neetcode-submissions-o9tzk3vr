class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        water = 0

        while left < n:
            # skip until we find a valid left wall (local peak)
            if left + 1 < n and height[left] < height[left + 1]:
                left += 1
                continue

            right = left + 1
            stones_between = 0
            best_right = -1
            stones_before_best_right = 0

            while right < n:
                if height[right] >= height[left]:
                    # ideal right wall found, calculate water directly
                    water += min(height[left], height[right]) * (right - left - 1) - stones_between
                    stones_between = 0
                    left = right
                    best_right = -1
                    right += 1

                else:
                    # right wall shorter than left, track it as candidate
                    stones_between += height[right]

                    is_first_candidate = best_right == -1
                    is_taller_than_best = best_right != -1 and height[right] > height[best_right]

                    if is_first_candidate or is_taller_than_best:
                        best_right = right
                        stones_before_best_right = stones_between - height[right]

                    right += 1

            # no ideal right wall found, settle for tallest candidate
            if best_right != -1:
                water += min(height[left], height[best_right]) * (best_right - left - 1) - stones_before_best_right
                left = best_right
            else:
                left += 1

        return water