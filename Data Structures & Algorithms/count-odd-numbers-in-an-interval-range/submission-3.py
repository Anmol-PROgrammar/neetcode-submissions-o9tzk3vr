class Solution:
    def countOdds(self, low: int, high: int) -> int:
        oddTillHigh = high // 2
        if high % 2 != 0 or high == 1:
            oddTillHigh += 1

        oddTillLow = low // 2
        
        # print(f"oddTillHigh: {oddTillHigh}, oddTillLow: {oddTillLow}")

        return oddTillHigh - oddTillLow
