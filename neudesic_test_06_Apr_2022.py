T = int(input())
if T in range(1001):
    pass
else:
    T = int(input())

num = []
for i in range(T):
    N = int(input())
    if N in range(1,10**9+1):
        num.append(N)
    else:
        N = int(input())

def special(T, num):
    prime_num = []
    prime = list(range(2,10**3))
    for i in prime:
        for j in range(2,i-1):
            if i%j==0:
                break
        else:
            prime_num.append(i)
    prime_num.remove(2)
    prime_num.remove(7)

    for i in num:
        for j in prime_num:
            if i%j==0:
                print('Regular')
                break
        else:
            print('Special')
            
special(T, num)
