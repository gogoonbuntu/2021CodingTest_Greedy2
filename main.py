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
#실패. if elem==a[0] 체크로직에서, 그냥 숫자가 같은 숫자면 그 숫자로 돌아가버림;
