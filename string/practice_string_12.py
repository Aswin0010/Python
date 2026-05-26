s1=input("Enter the string1: ").lower()
s2=input("Enter the substring : ")
if s2 in s1:
    print(s2," is substring of",s1)
else:
    print(s2,"is not the substring of",s1)    