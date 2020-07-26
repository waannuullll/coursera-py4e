# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
text = fh.read()
text_upper = text.upper().rstrip()
print(text_upper)
