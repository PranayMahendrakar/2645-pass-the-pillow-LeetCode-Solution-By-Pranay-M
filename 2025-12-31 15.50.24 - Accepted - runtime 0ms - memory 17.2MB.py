class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # One full cycle is 2*(n-1) seconds (go to end and back)
        cycle = 2 * (n - 1)
        time = time % cycle
        
        # If time <= n-1, moving forward (1 to n)
        # Otherwise, moving backward
        if time <= n - 1:
            return 1 + time
        else:
            return n - (time - (n - 1))