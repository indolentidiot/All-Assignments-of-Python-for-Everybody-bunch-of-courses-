# Asking and storing users work hours
hrs = input("Enter Hours:")
h = float(hrs)
# Asking and storing users pay per work hour
rate = input("Enter Rate:")
rt = float(rate)

# case:1 if workhours are less than 40
if (h <= 40):
    # Pay=no of work hours * pay rate
    Pay = h * rt

# case:1 if workhours are less than 40
else:
    addh = h - 40
    # additional pay=hours greater than 40*1.5 times the rate
    addPay = addh * 1.5 * rt

    # Pay=(no of work hours(for first 40 hours) * pay rate)+additional pay
    Pay = 40 * rt + addPay

    print(Pay)