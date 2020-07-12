largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            nm = int(num)
            print(nm)
            for i in nm:
                if (largest == None):
                    largest = nm
                elif largest > nm:
                    largest = nm


                else:
                    largest = largest
                if (smallest == None):
                    smallest = nm
                elif (smallest > nm):
                    smallest = nm
                else:
                    smallest = smallest

        except:
            print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)