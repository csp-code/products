import os 

# 讀取檔案
def read_file(filename):
	products=[]
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #這迴中止，繼續下一迴
			#-----------------------------------
			# 方法一
			#s=line.strip().split(',')  #strip()去換行符號
			#name=s[0]
			#price=s[1]
			# 方法二
			#name, price=line.strip().split(',')
			#-----------------------------------
			name, price=line.strip().split(',')  #字串切割
			products.append([name, price])
	return(products)

#讓使用者輸入
def user_input(products):
	while True:
		name=input('請輸入商品名稱：')
		if name =='q':
			break
		str1='請輸入'+name+'價格：'
		price =input(str1)
		price = int(price)  #將price轉換為整數型態
		#方法一
		#p=[]
		#p.append(name)
		#p.append(price)
		#product.append(p)
	    #方法二
	    #p=[name, price]
	    #product.append(p)
	    #方法三
		products.append([name, price])
	print(products)
	print('取第2個商品及價格值：',products[1][0],',',products[1][1])
	print('--------------------')
	return(products)

# 印出所有購買紀錄
def print_products(products):
	print('取每一個二維清單的值')
	i=0
	for p in products:
		print('第',i,'index:',p)
		print(p[0],'的價格是', p[1])
		i=i+1

# 寫入檔案
def write_file(filename,products):
	with open(filename, 'w', encoding='utf-8') as f:  #開啟檔案
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0]+ ','+ str(p[1])+ '\n')	  #寫入檔案, 且將p[1]由整數型態轉換為字串


def main():
	filename='products.csv'
	products=[]
	if os.path.isfile(filename):    #檢查檔案在不在，檢查相對路徑內，是否有此檔案!~~
		products=read_file(filename)
		print('找到檔案')
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file(filename,products)

main()