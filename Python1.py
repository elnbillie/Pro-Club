
def penjumlahan_angka(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == (target):
                if arr[i] != arr[j]:
                    if arr[i] < arr[j]:
                        return [i,j]
                    
asoy=list(map(int,input().split()))
targett=int(input())
print(penjumlahan_angka(asoy,targett))
        