def kthDivisible(a,b,d,k):
    nums=[]
    for i in range(a-1,b):
        if i%d==0:
            nums.append(i)
    if k>b:
        print("0")         
    print(nums[k])   
       
kthDivisible(10,30,3,4) 

    