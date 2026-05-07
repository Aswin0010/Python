lst=list(map(int,input("Enter numbers : ").split()))
k=int(input("Enter the value of k : "))
left=0
ans=0
s=0
atmost_k=0
atmost_k_1=0
if k!=0:
    for right in range(len(lst)):
        ch=lst[right]
        s+=ch
        while s>k:
            s-=lst[left]
            left+=1
        atmost_k+=(right-left+1)
    s=0
    left=0
    for right in range(len(lst)):
        ch=lst[right]
        s+=ch
        while s>k-1:
            s-=lst[left]
            left+=1
        atmost_k_1+=(right-left+1)
    print(atmost_k-atmost_k_1)        
else:
    for right in lst:
        if right==0:
            count+=1
            ans+=count
        else:
            count=0
    print(ans)        