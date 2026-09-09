class CountDown:
    def __init__(self):
        self.current=5
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <1:
            raise StopIteration
        value=self.current
        self.current-=1
        return value
counter=CountDown()
for x in counter:
    print (x)