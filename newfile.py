#String length of a file
wel = "Welcome to python programming."
file = open("newfile.txt", "w")
length = file.write(wel)
print(length)
file.close()
file = open("newfile.txt", "r")
print(file.read())
file.close()