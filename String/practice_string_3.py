s=input("Enter the string : ").lower()
for i in range (len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        print(s,"is not palindrome")
else:
    print(s,"is palindrome")