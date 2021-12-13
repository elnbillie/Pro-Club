def numbers(angka):
    output=[]
    for x in angka:
        if x not in output:
            output.append(x)
        else:
            output.remove(x)
    return output

num= int(input())
mun = list(map(int, str(num)))
print(numbers(mun))