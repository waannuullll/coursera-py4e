def computepay(h,r):
    if h <= 40:
        return (h*r)
    else:
        return (40*r+(h-40)*r*1.5)

hrs = float(input("Enter Hours:"))
rph = float(input("Input rate per hour:"))
p = computepay(hrs,rph)
print("Pay",p)
