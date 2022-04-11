def fbo(n):    
    n1=0
    n2=1    
    if(n>0):    
         n3 = n1 + n2    
         n1 = n2    
         n2 = n3    
         print(n3)    
         fbo(n-1)               
n=int(input())
print("0\n1")    
fbo(n-2)    
   
