
product=[]
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
	product.append([name, price])
print(product)
print('取第2個商品及價格值：',product[1][1])