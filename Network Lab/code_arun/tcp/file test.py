# with open("summa.txt", "rb") as f:
#     for i in f:
#         print(i)
    
f = open("summa.txt", "rb")

with open("summa2.txt", "wb+") as f2:
    for i in f:
        f2.write(i)
    print("File Copied")
    
f.close()


with open("summa2.txt", "rb+") as f2:
    for i in f2:
        print(str(i))
        