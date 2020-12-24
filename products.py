
products=[]
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
print('取每一個二維清單的值')
i=0
for p in products:
	print('第',i,'index:',p)
	print(p[0],'的價格是', p[1])
	i=i+1

with open('products.csv', 'w', encoding='utf-8') as f:  #開啟檔案
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+ ','+ str(p[1])+ '\n')	  #寫入檔案, 且將p[1]由整數型態轉換為字串
