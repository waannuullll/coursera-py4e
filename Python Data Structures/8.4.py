fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    awal = line.split()
    for kata in awal:
        if kata not in lst:
            lst.append(kata)

lst.sort()
print(lst)
