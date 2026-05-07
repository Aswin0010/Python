s=input("Enter Elements : ")
k=int(input("Enter the value of k: "))
left=0
freq={}
max_len=0
freq2={}
count=0
left2=0
for right in range (len(s)):
    ch=s[right]
    freq[ch]=freq.get(ch,0)+1
    freq2[ch]=freq2.get(ch,0)+1
    while len(freq)>k:
        freq[s[left]]-=1
        if freq[s[left]]==0:
            del freq[s[left]]
        left+=1
    while len(freq2)>k-1:
        freq2[s[left2]]-=1
        if freq2[s[left2]]==0:
            del freq2[s[left2]]
        left2+=1 
    count+=(left2-left)
if count:
    print(count)
else:
    print("no count")    