import random
b = ['布', '剪刀', '石頭']
a = random.choice(b)
while True:
	c = input ('剪刀石頭布，請出拳：')
	if c != '布' and c != '剪刀' and c != '石頭':
		print ('請輸入 剪刀/石頭/布 唷')
		continue
	else:
		break
print ('我出的是', a)
if a == c:
	print ('平手!')
elif (c == '布' and a == '石頭') or (c == '剪刀' and a == '布') or ( c == '石頭' and a == '剪刀'):
	print ('恭喜你贏啦!')
else:
	print ('真可惜~再接再厲吧!')