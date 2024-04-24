a = 12345
a = str(a)
l = []

for i in a:
    l.append(int(i))

k = str(sum(l))

if(len(k)>1):
    l = []
    for i in k:
        l.append(int(i))

print(sum(l))