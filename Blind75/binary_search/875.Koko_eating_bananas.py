class Solution:
    def checkIt(self, array: list[int], t: int) -> int:
        val = 0
        for i in array:
            val += (i + t - 1) // t  # This calculates the number of hours needed at speed t
        return val

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        start, end = 1, max(piles)  # Koko can eat at least 1 banana per hour, max is the biggest pile
        smallest = end  # Start with the maximum possible speed

        while start <= end:
            midpoint = (start + end) // 2  # Possible eating speed
            check = self.checkIt(piles, midpoint)  # Check if we can finish in h hours

            if check <= h:
                smallest = midpoint  # Update minimum possible speed
                end = midpoint - 1  # Try a smaller speed
            else:
                start = midpoint + 1  # Increase speed to finish faster

        return smallest
