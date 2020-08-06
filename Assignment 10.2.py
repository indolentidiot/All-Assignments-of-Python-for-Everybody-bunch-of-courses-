#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.



lst=list()
times=dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    words=line.split()
    for word in words:
        if word=="From":
            i=words.index(word)
            t=words[i+5]
            time=t.split(':')
            
            times[time[0]]=times.get(time[0],0)+1

val=sorted([(time,counts )for time ,counts in times.items() ])
for i in range(len(val)):
    print(val[i][0],val[i][1]) 
