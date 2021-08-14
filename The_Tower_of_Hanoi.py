#The Tower of Hanoi
"""
The Tower of Hanoi (also called the Tower of Brahma or Lucas's Tower and sometimes pluralized) 
ís a mathematical game or puzzle.

It consists of three rods and a number of disks of different sizes, 
which can slide onto any rod. 
The puzzle starts with the disks in a neat stack in ascending order of size on one rod, 
the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1.Only one disk can be moved at a time.
2.Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack
3.No disk may be placed on top of a smaller disk
"""
# source rod 
A = []
# middle rod
B = []
# target rod 
C = []

def showAll():
    print(A, B, C, '_________________', sep = '\n');

def move(n, source, target, bridge):
    if n > 0:
        # move n - 1 disks from source to bridge, so they are out of the way
        move(n - 1, source, bridge, target)
        
        # move the nth disk from source to target
        target.append(source.pop())
        
        # Display our progress
        showAll()
        
        # move the n - 1 disks that we left on bridge onto target
        move(n - 1, bridge, target, source)

discs = int(input("Enter number of disks: "))
print(discs, '_________________', sep = '\n');
A = list(range(1, discs+1))[::-1]
showAll()
# initiate call from source A to target C with auxiliary B
move(discs, A, C, B)
print("Number of moves:" + str(2**discs - 1))
