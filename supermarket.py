class Products:
	from datetime import datetime
	def __init__(self, price, name, is_vol): # is_vol = w - weght, s - sh, v - vol
		self.price = price
		self.is_vol = is_vol
		self.name = name

class Cash:
	from datetime import datetime
	total = {}
	tot = 0
	def Buy(self, product, sum):
		if product not in self.total:
			self.total.update({product: sum})
		else:
			self.total.update({product: self.total[product] + sum})
	def GetCheck(self):
		is_volume = {'w': 'kg', 's': 'st', 'v': 'l'}
		print ('*'*45)
		print(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))
		print ('*'*45)
		for key, value in self.total.items():
			if key.is_vol != 's':
				print('{:10}${:3} * {:5}{:2} = ${}'.format(key.name, key.price,value, is_volume[key.is_vol], key.price * value))
				self.tot += key.price * value
			else:
				print('{:10}${:3} * {:5}{:2} = ${} inc disc 5%'.format(key.name, key.price,value, is_volume[key.is_vol], (key.price * value) * 0.95))
				self.tot += key.price * value
		print ('*'*45)
		print('TOTAL: ${}'.format(self.tot))
		print ('*'*45)
from datetime import datetime
A = Products(100, 'kartoshka', 'w')
B = Products(200, 'Cok', 'v')
C = Products(340, 'Chocolate', 's')
D = Cash()
D.Buy(A, 0.3)
D.Buy(B, 0.3)
D.Buy(C, 1)
D.Buy(C, 1)
D.Buy(C, 1)
D.GetCheck()
