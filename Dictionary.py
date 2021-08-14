#dictionary
squares = {1: 1, 2: 4, 3: "error_code", 4: 16,}
squares[8] = 64
squares[3] = 9
squares[1] = 111
squares[1] = 1
print(squares)

#'in' and 'not in' 
num = {
    1: "One",
    2: 'Two',
    3: "Three",
}
print(1 in num)
print("Two" in num)
print(4 not in num)
print(5 in  num)
print('Two' in num)
print(num[2])
print('2' in num)

#get function
pairs = {1: "apple",
"orange": [2, 3, 4], 
'True': False, 
None: 'True',
}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, 'not in pairs'))
print(pairs.get(True))
print(pairs.get(None))

keys = pairs.keys()

values = pairs.values()

for k in pairs.keys():
    print(pairs[k])




text1 =  input('First text: ')
text2 = input('Second text: ')
for text in [text1,text2]:
    if 'a' in text and 'e' in text and 'i' in text and 'o' in text and 'u' in text:
        print('YES')
    else:
        print('NO')

        










