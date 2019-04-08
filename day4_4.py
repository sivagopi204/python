def program1():
	n = int(input("Enter a Positive Value::::----"))
	l = []
	l.append(n)
	if n>1:
		while n > 1:
			if n%2 == 0:
				n = int(n/2)
				l.append(n)
			else:
				n = int((3*n)+1)
				l.append(n)

	print("Length Of the Series: %s"%len(l), "And Values Are: %s"%l)

if __name__ == '__main__':
	program1()
