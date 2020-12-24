
products=[]
while True:
	name=input('請輸入商品名稱：')
	if name =='q':
		break
	str1='請輸入'+name+'價格：'
	price =input(str1)
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