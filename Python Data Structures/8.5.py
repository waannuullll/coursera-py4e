fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    kalimat = line.split()
    if 'From' in kalimat:
        print(kalimat[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
