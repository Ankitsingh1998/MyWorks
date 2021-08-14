#Object Lifecycle
a = 42  # Create object <42>
b = a  # Increase ref. count  of <42> 
c = [a]  # Increase ref. count  of <42> 
print(a,b,c)
del a  # Decrease ref. count  of <42>
b = 100  # Decrease ref. count  of <42> 
c[0] = -1  # Decrease ref. count  of <42>
a = ['String','word','play','python']
print(a,b,c)
a[0] = 45
print(a)

a[0] = 'string1'
print(a)
a.remove(a[0])
print(a)
a.insert(0,'string2')
print(a)
a[1] = 'word1'
a.insert(4,'fun')
a.insert(5,'word1')
print(a)
print(a.count('word1'))
a.reverse()
print(a)







