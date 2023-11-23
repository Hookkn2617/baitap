snt =[]

def timsonguyento(so):
    for i in range(0, so):
        if(checksonguyento(i) == True):
            snt.append(i)

def checksonguyento(so):
    if(so < 2):
        return False

    for i in range(2, so):
        if(so % i == 0):
            return False
    return True

n = int(input())

timsonguyento(n)

if(len(snt) <= 0):
    print("ko co snt nao nho hon ", n)
else:
    print("cac snt nho hon n la: ",end="")
    for i in snt:
        print(i,end=", ")
