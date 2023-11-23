dung = 0

for i in range(1, 11):
    print("go dap an cua 6 x",i," hoac nhap boqua hoac nhap dunglai : ")
    dapan = input()
    if(str(dapan) == "boqua"):
        print("bo qua")
        continue
    elif(str(dapan) == "dunglai"):
        break
    elif(str(dapan) == str(6*i)):
        print("tra loi dung")
        dung += 1
        continue
    else:
        print("Tra loi sai")
        continue
    
print("tong cong tra loi duoc ", dung, "cau")