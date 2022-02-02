def main():
	a = list(map(int, input()))
	for idx, val in enumerate(a):
		if idx == 0:
			prevElem = val
			continue
		print("elem:",val)
		if prevElem<=1 or val<=1:
			prevElem += val
		else : prevElem *= val
		print("now:",prevElem)		
	return prevElem

print(main())
