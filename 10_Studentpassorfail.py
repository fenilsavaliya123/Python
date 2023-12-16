a1=int(input("enter a sub1 mark:"))
a2=int(input("enter a sub2 mark:"))
a3=int(input("enter a sub3 mark:"))


ans=((a1+a2+a3)/300)*100
print("result is :",ans)

if(ans>33):
    print("pass")
else:
    print("fail")    