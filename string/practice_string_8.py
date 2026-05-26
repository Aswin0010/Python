s1=input("Enter the string1: ")
s2=input("Enter the string2: ")
if len(s1)!=len(s2):
    print("not anagram")
else:    
    freq={ }
    for i in s1:
        freq[i]=freq.get(i,0)+1
    for j in s2:
        freq[j]=freq.get(j,0)-1
    if all(v==0 for v in freq.values()):
        print("They are anagram")
    else:
        print("They are not anagrams")        