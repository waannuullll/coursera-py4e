largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        else:
            num = int(num)
            if largest is None:
                largest = num
            elif largest < num:
                largest = num
            if smallest is None:
                smallest = num
            elif smallest > num:
                smallest = num
    except:
        print('Invalid input')
print("Maximum is", largest)
print('Minimum is', smallest)
