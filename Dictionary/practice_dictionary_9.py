lst=list(map(int,input("Enter numbers : ").split()))
k=int(input("Enter the value of k : "))
left=0
count=0
atmost_k=0
atmost_k_1=0
for right in range(len(lst)):
    ch=lst[right]
    if ch%2!=0:
        count+=1
    while count>k:
        if lst[left]%2!=0:
            count-=1
        left+=1
    atmost_k+=(right-left+1)
count=0
left=0
for right in range(len(lst)):
    ch=lst[right]
    if ch%2!=0:
        count+=1
    while count>k-1:
        if lst[left]%2!=0:
            count-=1
        left+=1
    atmost_k_1+=(right-left+1)
print(atmost_k-atmost_k_1)            