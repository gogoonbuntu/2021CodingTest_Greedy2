# 0 1 2 3 4 와 같이 숫자를 입력 받으면, + 혹은 * 를 수행해 가장 큰 값을 만들어라
# 모두 곱하기를 먼저 한다. 0, 1 은 더하기가 이득이다.

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