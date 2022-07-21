def countDown(n): 
    print(n) 
    
    if n==0:
        return
    else:
        countDown(n-1);
countDown(5);