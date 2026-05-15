s=input("Enter the string : ").lower()
freq={ }
for i in range (len(s)-1):
    freq[s[i]]=freq.get(i,0)+1
print(freq)    