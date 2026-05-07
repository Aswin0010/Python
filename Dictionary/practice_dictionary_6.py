s=input("Enter Elements : ")
left=0
last_seen={}
max_len=0
longest=""
for right in range (len(s)):
    ch=s[right]
    if ch in last_seen and last_seen[ch]>=left:
        left=last_seen[ch]+1
    last_seen[ch]=right    
    if max_len<right-left+1:
        max_len=right-left+1
        longest=s[left:right+1]   
print(longest)