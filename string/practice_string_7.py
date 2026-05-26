s=input("Enter the string : ")
freq={ }
for i in s:
    freq[i]=freq.get(i,0)+1
print(max(freq,key=freq.get))    