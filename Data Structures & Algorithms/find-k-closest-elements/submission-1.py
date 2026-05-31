class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distanceToX, ans = [],[]
        for i in range(len(arr)):
            distanceToX.append(abs(x-arr[i]))
        print(distanceToX)
        
        counter = 0

        # Find the minimum value
        min_value = min(distanceToX)

        # Find its first index
        min_index = distanceToX.index(min_value)
        ans.append(arr[min_index])
        counter+= 1

        i,j = min_index - 1, min_index + 1
        while counter != k:
            if i < 0:
                ans.append(arr[j])
                j += 1
            elif j >= len(arr):
                ans.append(arr[i])
                i -= 1
            elif distanceToX[i] <= distanceToX[j]:
                ans.append(arr[i])
                i -= 1
            else:
                ans.append(arr[j])
                j += 1

            counter += 1


        return sorted(ans)





