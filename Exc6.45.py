x=int(input())
if x>0:
    
    
    print("A",end=" ")
    if x==2:
        print("S",end=" ")
        x=int(input())
        if x==2:
            print("A",end=" ")
            x=int(input())
            if x==3:
                print("P",end=" ")
                
            elif x==1:
                print("R",end=" ")  
                  
        elif x==3:
            print("T",end=" ")
            x=int(input())
            if x==2:
                print("A",end=" ")
                x=int(input())
                if x==1:
                    print("R",end=" ")
            elif x==1:
                print("R",end=" ")
    elif x==1:
        print("*")        
elif x==0:
    print("invalid password")            