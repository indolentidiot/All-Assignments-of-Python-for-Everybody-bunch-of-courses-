#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
#solution

text = "X-DSPAM-Confidence:    0.8475";
#loading the index value of 0 into variable ind
ind=text.find("0")
#loading the sliced text into variable num
num=text[ind:ind+6]
#typecasting stored text to float
flt=float(num)
#printing the num
print(flt)