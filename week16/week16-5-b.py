a,b=list(map(int,input().split()))
ans=0
for n in range(a,b+1):
	bad=0
	for i in range(2,n):
		if n%i==0:bad=1
	if bad==0:ans+=1


print(ans)