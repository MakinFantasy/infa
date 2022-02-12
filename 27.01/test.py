class Flat_Iterator:
    def __init__(self, target):
        self.target = target

    def __iter__(self):
        self.i = -1
        self.p = []
        return self

    def __next__(self):
        self.i += 1

        inside_counter = 0
        focus = self.target
        while inside_counter < len(self.p):
            p_focus = focus[self.p[inside_counter]]
            if self.i - sum(self.p) < len(p_focus):
                focus = p_focus
                inside_counter += 1
            else:
                self.p.pop()
                self.i -= len(p_focus) - 1

        index = self.i - sum(self.p)
        if index >= len(self.target):
            raise StopIteration

        if index + 1 < len(focus) and type(focus[index + 1]) is list:
            self.p.append(index + 1)

        return focus[index]


if __name__ == "__main__":
    nested_list = [3, 5, [7, 4, 8, [54, 32, 43], 3], 1, 2]
    for e in Flat_Iterator(nested_list):
        print(e)