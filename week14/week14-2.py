#但是我們想慢慢理解 set() 到底怎麼用
s = [1,2,3,4] #大括號
print(s)

s = set((1,3,5,7)) # 第2種, 用set() 裡面放你一開始要加入的東西
print(s)

s = set([1,2,3,4]) # 第2種的 set() 裡面也可以做[方括號]list的陣列東西
print(s)

s = set('Hello') #第2種的 set() 裡面也可以做[字串]會把他一個個拆開來
print(s)

#下面試試 .add() 和 .remove()
s.add(100)
print(s)
s.remove('H')
print(s)