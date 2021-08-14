file = open("books.txt", "r")
#your code goes here
booklist = file.readlines()

for bookname in booklist:
    split_words = bookname.split()
    for word in split_words:
        print(word[0],end='')
    print('')

file.close()


#Wrong approach:
"""
file = open("books.txt", "r")

booklist = file.readlines()
create_booklist = []
for bookname in booklist:
    book_words_split = bookname.split()
    create_booklist.append(book_words_split)  
print(create_booklist)

for lists in create_booklist:
    for x in range(1,len(lists)):
        lists[x][0] = lists[x][0] + lists[x-1][0]
        result = lists[x][0]
    print(result)
file.close()
"""

"""
lists[x][0] = lists[x][0] + lists[x-1][0]
TypeError: 'str' object does not support item assignment
"""









