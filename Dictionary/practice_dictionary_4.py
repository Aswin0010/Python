s=input("Enter String : ").lower()
k=int(input("Enter the top number : "))
freq={}
a=[]
for ch in s:
    freq[ch]=freq.get(ch,0)+1
a=sorted(freq.items(),key=lambda x:x[1],reverse=True)
for i in range(k):
    print(a[i])