a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=0
for i in range(0,a):
	print(b[i]+c[i],end=' ')