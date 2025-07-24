import heapq


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.low = []  # max heap for lower half of numbers
        self.high = []  # min hea for upper half of numbers

    def add_num(self, num):
        """
        Adds a number into the data structure.
        Args:
            num (int): The number to add.
        """
        # add to lower heap first
        heapq.heappush(self.low, -num)

        # ensure every number in low <= ever number in high
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # balance sizes
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

        # if lower heap has more elems

    def find_median(self):
        """
        Returns the median of all elements so far.
        Returns:
            float: The median value.
        """
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2
