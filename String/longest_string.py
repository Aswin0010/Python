s1=input("Enter the string1: ").split()
if len(s1)>0:
    count_long=s1[0]
    for i in s1[1:]:
        if len(count_long)<len(i):
            count_long=i
    print(count_long,"is the longest word")    
else:
    print("no string")    
