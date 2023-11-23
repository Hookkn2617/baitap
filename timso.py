uoc = []

def timsouoc(so):
    for i in range(1, so+1):
        if(so%i == 0):
            uoc.append(i)

def checksothuannghich(so):
    songuoc = str(so)[::-1]
    if(songuoc == str(so)):
        return True
    return False


def checksohoanhao(so):
    sum = 0
    for i in uoc:
        sum += i
    if(sum == so):
        return True 
    return False

n = int(input("nhap so n: "))

timsouoc(n)

if any(i**2 == n for i in range(0,n + 1)):
    print(n, " la so chinh phuong")
if(len(uoc) == 2 and n >= 2):
    print(n," la so nguyen to")
if(checksohoanhao(n) == True):
    print(n, "la so hoan hao")
if(checksothuannghich(n) == True):
    print(n, "la so thuan nghich")
