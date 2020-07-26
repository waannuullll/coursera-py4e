name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

complete_dict = dict()
complete_list = list()

for line in handle:
    text = line.split()
    if 'From' in text:
        hour = text[5].split(':')[0]
        complete_dict[hour] = complete_dict.get(hour,0) + 1

complete_list = complete_dict.items()
complete_list = sorted(complete_list)

for x in complete_list:
    print(x[0],x[1])
