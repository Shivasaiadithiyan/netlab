l = [38,63,48,58,55,3,30,14,23,9,21,51,16,45,54,60,49,19,303,31,52,56,15,44,42,11,12,27,29,53,50,2,41,6,24,65,1,5,302,13]
l.sort()
print(l)
a = []
for i in range(1,66):
    if i not in l:
        a.append(i)
        
print(a)