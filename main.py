def main():
	a = list(map(int, input()))
	for elem in a:
		if elem == a[0]:
			prevElem = a[0]
			continue
		print("elem:",elem)
		if prevElem<=1 or elem<=1:
			prevElem += elem
		else : prevElem *= elem
		print("now:",prevElem)		
	return prevElem

print(main())
