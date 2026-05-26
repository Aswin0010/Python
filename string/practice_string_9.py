s1=input("Enter the string1: ")
freq={ }
for i in s1:
    freq[i]=freq.get(i,0)+1
for i in s1:
    if freq[i]==1:
        print(i,"is the first non repeating character")
        break
else:
    print("no non repeating character")
        