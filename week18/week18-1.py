Class Solution:
	def halvesAreAlike(self,s,str)->bool:
		N=len(s) #字串的長度
		a=s[:N//2] #前半段
		b=s[N//2:] #前半段
		motherA=0  #a的母音有幾個
		morther=0  #a的母音有幾個
		for c in a:
			if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
				motherA+1
			if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
				motherA+=1
		for c in b:
			if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
				motherB+=1
			if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
				motherB+=1
		if motherA==motherB:return True
		else:return False