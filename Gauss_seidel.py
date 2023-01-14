def Gauss_seidel(a, x ,b,e,iteration=1):    
    n = len(a)                   
    x_0=tuple(x)
    x_1=x
    
    for j in range(0, n):      
        d = b[j]                  
        for i in range(0, n):     
            if(j != i):
                d-=a[j][i] * x_1[i]     
        x_1[j] = d / a[j][j]
    print('iteration',iteration)
    print(x_1)
    trouve=True
    for i in range(len(x)):
            if (abs(x_1[i]-x_0[i])<=e):
              trouve=False
        
    if (trouve==True):
        Gauss_seidel(a, x ,b,e,iteration=iteration+1)
                 
   
a=[[3,1,-1],[1,5,2],[2,-1,-6]]
b=[2,17,-18]
x=[0,0,0]
print(x)
x = Gauss_seidel(a, x, b,0.0000000000000001)  
            
