s = '00111'
N =len(s) #長度
zero = 0 #等一下也要
one = 0 #想找出全部的1
for i in range(N):
  if s[i]=='1':one += 1 #如果是1,全部加起來
#現在知道共有機個 one
#print('一開始的時候,都在右邊,統計結果',zero',zero,'one',one)
ans=0
for i in range(N-1): #要逐格去做修正,吐出一格,看他是多少,就修正
  if s[i]=='0': #吐出0,給左邊
      zero +=1 #左邊多一個0
  if s[i]=='1':
      one -=1
  print('中間過程中','zero',zero,'one',one)
  ans = max(ans,zero+one) #最好的答案,最大的值
print('答案出來了',ans)