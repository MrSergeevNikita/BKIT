class Unique:
    def __init__(self, spisok, **kwargs):
        self.data = spisok
        self.used_elements = set()
        self.i = 0
        self.ignore_case = len(kwargs)
    def __iter__(self):
        return self
    def __next__(self):
        while (self.i < len(self.data)):
            if isinstance(self.data[self.i], str):
                if self.ignore_case == 1:
                    s = self.data[self.i].lower()
                else:
                    s = self.data[self.i]
                if s not in self.used_elements:
                        self.used_elements.add(s)
                        return s
            else:
                if self.data[self.i] not in self.used_elements:
                    self.used_elements.add(self.data[self.i])
                    return self.data[self.i]
            self.i += 1
        self.i = 0
        raise StopIteration