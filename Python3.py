def jumlah(x):
    dic = {}
    for i in x:
        if i not in dic.keys():
            dic[i]=1
        else:
            dic[i]+=1
    return dic

a=input()
arr=list(a)
b=jumlah(arr)
b=dict(sorted(b.items(), key=lambda x:x[1]))
for i in b:
    print(i+":",b[i])
