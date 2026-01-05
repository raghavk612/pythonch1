n=int(input())

x=[]
sum=0
for i in range(n):
	x.append(int(input()))
k=str(input())
for j in range(len(x)):
	x[j]=str(x[j])
	if k in x[j]:
		sum+=int(x[j])
print(sum)