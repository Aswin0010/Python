s1=input("Enter the string1: ")
count=0
if len(s1)>0:
    print("The substring are :")
    for i in range (len(s1)):
        for j in range (i,len(s1)):
            print(s1[i:j+1])
            count+=1
    print("Number of substring is : ",count)        
else:
    print("no substring")    