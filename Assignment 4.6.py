def computepay(h, r):
    if (h > 40):
        hours = h - 40
        extrapay = hours * r * 1.5
        pay = 40 * r + extrapay

    else:
        pay = h * r
    return pay


hrs = input("Enter Hours:")
try:
    h = float(hrs)

except:
    print('ENTER VALID NUMBER')
rate = input("Enter Hours :")
try:
    r = float(rate)
except:
    print('ENTER VALID NUMBER')
p = computepay(h, r)
print("Pay", p) 