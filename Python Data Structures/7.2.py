# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
num_lines = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        ind = line.find('0')
        num_float = float(line[ind:])
        total = total + num_float
        num_lines = num_lines + 1
print('Average spam confidence:',total/num_lines)
