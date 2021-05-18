class Repeat:
    def __init__(self, ranges):
        """
        ranges: (
            ("val1", min1, max1),
            ("val2", min2, max2),
            ...
        )
        """
        self.ranges = ranges
        self.count = 0

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        self._index += 1
        for i in self.ranges:
            a = self.ranges
            if self._index > len(self.ranges):
                raise StopIteration
        return a

def test():
    ranges = [
        ("i", 2, 3),
        ("j", 2, 3),
        ("k", 3, 5),
    ]

    repeator = Repeat(ranges)

    for info in repeator:
        print(info)

    for i in range(2, 4):
        for j in range(2, 4):
            for k in range(3, 5 + 1):
                print("i", i, "j", j, "k", k)

if __name__ == "__main__":
    test()
