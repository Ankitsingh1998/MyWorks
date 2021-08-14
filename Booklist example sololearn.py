#example - file
file = open("books.txt", "r")

#your code goes here
a = file.readlines()

#for index value 0 to [len(a)-1]:
x = 0
for x in range(len(a) - 1):
    a[x] = a[x]
    print(a[x][0] + str(len(a[x])-1))

#for last value:
print(a[len(a)-1][0] + str(len(a[len(a)-1])))

file.close()

#Booklist_example_sololearn
Booklist = ['Harry Potter' , 'Pride and Prejudice' , 'Sherlock Holmes' , 'Papillion' , 'Benjamin Franklin']

x = 0
for x in range(len(Booklist)):
    Booklist[x] = Booklist[x]
    print(Booklist[x][0] + str(len(Booklist[x])))
    continue
