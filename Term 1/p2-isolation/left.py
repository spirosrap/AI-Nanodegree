def left(capital):
	for i in range(0,10):
		capital = capital - (capital * 0.05)
	return capital	
print(left(1000))

