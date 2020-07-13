#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt
# Use words.txt as the file name
#check for a valid file name and proceed
try :
    fname = input("Enter file name: ")
    fh = open(fname)
except :
    print("USE A VALID FILE")
    quit()
#Read the contents of given file
rd=fh.read()
#Eliminate unwanted newline chars
strp=rd.rstrip()
#Convert text to upper case
upcs=strp.upper()
#print the conv text
print(upcs)