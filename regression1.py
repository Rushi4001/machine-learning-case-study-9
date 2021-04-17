import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def LinearRegrasion():
    x=[1,2,3,4,5]
    y=[3,4,2,4,5]
    
    print("values of Independent of variables x",x)
    print("values of dependent of variables y",y)
    
    # Least square method
    mean_x=np.mean(x)
    mean_y=np.mean(y)
    
    print("mean of Independent variable x",mean_x)
    print("mean of dependent varieble y",mean_y)
    n=len(x)
    
    numerator=0
    denomenator=0
    
    # Equation of line is y=mx+c
    
    for i in range(n):
        numerator=numerator+((x[i]-mean_x)*(y[i]-mean_y))
        
        denomenator=denomenator+((x[i]-mean_x)**2)
        
    m=numerator/denomenator
    
    # c=y'-mx'
   
    c = mean_y-(m*mean_x)
    
    print("slope of regression line is ",m)     #0.4
    print("y intercept of regression line is :",c)   #2.4
    
    #Display plotting of above points
    x=np.linspace(1,6,n)
    
    y=c + m * x
    
    plt.plot(x,y,color='#58b970',label='regression Line')
    
    plt.scatter(x,y,color='#ef5423',label='scatter plot')
    
    plt.xlabel('x-Independent variable')
    plt.ylabel('y-dependent variable')
    
    plt.legend()
    plt.show()
    
    #findout goodness of fit ie R square
    ss_t=0
    ss_r=0
    
    for i in range(n):
        y_pred=c + m * x[i]
        ss_t+=(y[i]-mean_y)**2
        ss_r+=(y[i]-y_pred)**2
        
    r2=1-(ss_r/ss_t)
    
    print("Goodness of fit using R2 methods is",r2)
        
def main():
    print("___supervised machine learning___")

    print("___ linear regression___")
    
    LinearRegrasion()

if __name__ =="__main__":
    main()