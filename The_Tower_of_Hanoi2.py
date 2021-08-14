#The Tower of Hanoi
"""Towers of Hanoi
Visual version
In SoloLearn, limited to 4-5 levels because of time processing for printing
"""

class hanoi():
    """Class representing all 3 towers
    Includes a textual printing method
    and allows to move any number of
    discs from a tower to another"""
    
    def __init__(self, levels):
        self.levels = levels
        self.base = "_"*(6*levels + 5)
        self.towers = [list(range(levels,0,-1)), [], []]

    def __repr__(self):
        text = "\n"
        for h in range(self.levels, -1, -1):
            for t in range(3):
                if len(self.towers[t]) <= h:
                    width = 0
                else:
                    width = self.towers[t][h]
                blank = self.levels - width
                text += (" "*blank +
                 "#"*width + "|" +
                 "#"*width + 
                 " "*(blank + 1))
            text += "\n"
        text += self.base
        return text


    def move_one(self, start, end):
        self.towers[end].append(
            self.towers[start].pop())
        print(self)


    def move(self, size=None, start=0, end=2):
        if size is None:
            size = self.levels
        if size == 1:
            self.move_one(start, end)
        else:
            inter = 3 - start - end
            self.move(size-1, start, inter)
            self.move_one(start, end)
            self.move(size-1, inter, end)


"""Main"""
try:
    yours = hanoi(int(input('Enter the number of disks: ')))
    print(yours)
    yours.move()
except:
    print("Enter an integer giving the height of the tower")