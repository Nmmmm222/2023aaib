N,M=list(map(int,input().split()))

if N%M==0:print(N//M,end='')
if N%M!=0:print(N//M+1,end='')