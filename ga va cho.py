
n, m = map(int,input("nhap lan luot so con va so chan: ").split())

g= 0
c= 0

for ga in range(1,n + 1):
    for cho in range(1,n - ga + 1):
        if(ga*2 + cho*4 == 100):
            g = ga
            c = cho
print("co", g, "ga va ", c, "cho")