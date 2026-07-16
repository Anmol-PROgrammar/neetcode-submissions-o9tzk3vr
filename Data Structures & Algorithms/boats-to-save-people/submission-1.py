class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i, j = 0, n - 1
        boat = 0

        while i <= j:
            if people[i] + people[j] <= limit:
                boat += 1
                i += 1
                j -= 1
            if people[i] + people[j] > limit:
                boat += 1
                j -= 1
        return boat
