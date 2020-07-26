name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

person_list = dict()

for line in handle:
    text = line.split()
    if 'From' in text:
        person_list[text[1]] = person_list.get(text[1],0) + 1

most_val = 0
for key in person_list:
    if person_list[key] > most_val:
        person = key
        most_val = person_list[key]
    
print(person, person_list[person])
