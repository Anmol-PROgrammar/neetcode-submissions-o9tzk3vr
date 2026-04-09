class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        res = 0
        while i < n:
            stone = 0
            if (i + 1) < n and (height[i] < height[i+1]):
                # print(f"finding best i: {height[i]}, {height[i+1]}")
                i += 1
                continue
            j = i + 1
            best_j = -1        # track best right wall index
            best_j_stone = 0   # track stone at that point
            temp_stone = 0
            while j < n:
                # print(f"finding best j: {height[i]}, {height[j]}")
                if height[j] < height[i]:
                    # print(f"    j is less than: {height[i]}, {height[j]}")
                    temp_stone += height[j]
                    # track best right wall (tallest j seen so far)
                    if best_j == -1 or height[j] > height[best_j]:
                        best_j = j
                        best_j_stone = temp_stone - height[j]  # stone before this j
                    j += 1
                elif height[j] >= height[i]:
                    # print(f"    before result {res}")
                    res += min(height[i], height[j]) * (j - i - 1)
                    res -= temp_stone
                    temp_stone = 0
                    stone = 0
                    # print(f"    after result {res} using {height[i]},{height[j]}")
                    i = j
                    best_j = -1
                    j += 1
            # j exhausted without finding wall >= height[i], settle for best_j
            if best_j != -1:
                # print(f"    settling with best_j: {height[i]}, {height[best_j]}")
                res += min(height[i], height[best_j]) * (best_j - i - 1)
                res -= best_j_stone
                i = best_j
            else:
                i += 1
        return res