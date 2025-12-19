print("Get max,min swap value of variables")
print("\n 1.max \n 2.min \n 3.swag")
a,b =map(int, input("enter two numbers").split(","))
choice = int(input("enter your choice"))
if(choice==1):
    print(max(a,b))
elif(choice==2):
    print(min(a,b))
elif(choice==3):
    a,b=b,a
    print ("After Swaping %d %d "%(a,b))
else:
    print("invalid choice")