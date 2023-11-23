fiboccani = []
socantim=[]

def checksonguyento(so):
    if(so < 2):
        return False

    for i in range(2, so):
        if(so % i == 0):
            return False
    return True

def timsofiboccani(so):
    a = 0
    b = 1
    fiboccani.append(a)
    fiboccani.append(b)
    while a < so or b < so:
        a += b
        if(a>so):
            break
        fiboccani.append(a)
        if(b>so):
            break
        b += a
        fiboccani.append(b)

def timsocantim():
    for i in fiboccani:
        if(checksonguyento(i) == True):
            socantim.append(i)

n = int(input())
timsofiboccani(n)
timsocantim()
print("so fiboccani va la so nguyen to nho hon", n," la: ",end="")
for i in socantim:
    print(i, end=",")
