class Repeat:
    def __init__(self, ranges):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration

class Demo:
    def __init__(self):
        self._max = 10

    def __iter__(self):
        # print("iter init")
        self._idx = 0
        return self

    def __next__(self):
        # print("iter next")
        self._idx += 1

        if self._idx > self._max:
            raise StopIteration

        return self._idx

def test():
    ranges = [
        ("i", 2, 3),
        ("j", 1, 2),
    ]

    # repeator = Repeat(ranges)
    repeator = Demo()

    for info in repeator:
        print(info)

if __name__ == "__main__":
    test()
