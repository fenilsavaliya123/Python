# def demo():
#     print("hello world")
    
    
# demo()   


# def demo(a,b):
#     ans=a+b
#     print(ans)  
    
# x=10
# y=12
# demo(x,y)  




# def demo(x):
#     p=(sum(x)/400)*100
#     return p
    
# x=[10,20,40,34]

# r=demo(x)
# print(r) 






# def abc():
#     return "hello world"


# print(abc())






# def _bigvsAandB(a,b):
#     if(a>b):
#         return a
#     else:
#         return b
    
    
# x=12
# y=23

# f1=_bigvsAandB(x,y)
# print(f1)


# x=34
# y=6
# f2=_bigvsAandB(x,y)
# print(f2)





# def _you(name):
#     p="hello "+ name
#     return p


# p=_you("fenil")
# print(p)





# def _you(name="gggg"):
#     p="hello "+ name
#     return p


# p=_you()
# print(p)





# def _factorial(n):
#     ans=1
#     for i in range(1,n+1):    
#       ans=ans*i
      
      
#     print(ans)
    


# p=_factorial(3)







# def bigwithinThree(a,b,c):
#     if(a>b):
#         if(a>c):
#             return a
#         else:
#             return c
#     else:
#         if(b>c):
#             return b
#         else:
#             return c
        
# f=bigwithinThree(67,83,102) 
# print(f)  
# c=bigwithinThree(67,83,0) 
# print(c)         
    
# (0°C × 9/5) + 32 = 32°F


# def _ferTocel(c):
#     f=c*(9/5)+32
    
#     return f

# demo=_ferTocel(12)

# print(demo)










# def _sumofnumFun(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n+_sumofnumFun(n-1)
    
    
# f=_sumofnumFun(5)
# print(f) 
   
n=15

for i in range(n):
    print("*"*(n-i))
        
   