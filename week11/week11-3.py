#國中沒有教,輾轉相除法 (減法 大約就是 除法取除數)
a = 123456789012
b = 98765432101

def ged(a,b): #上週教過 函式 的定義
  print(a,b) #想讓你看到過程,所以把a, b印出來
  if a==0: return b #終止條件,遇到0的話,另一邊是答案
  if b==0: return a #終止條件,遇到0的話,另一邊是答案
  return ged(b,a%b)

ans = ged(a,b) #同專業的 ged()函式 看答案是什麼
print(ans)