str=input("Enter the string : ").lower()
count=0
for i in str:
    if i in "aeiou":
        count+=1
print("The number of vowels in",str,"is",count)