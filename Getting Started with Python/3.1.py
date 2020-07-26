hrs = float(input("Enter Hours:"))
rph = float(input("Enter rate per hours:"))
if hrs <= 40:
    pay = hrs*rph
else:
    pay = 40*rph + (hrs-40)*1.5*rph
print(pay)
