def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def gcd_N(arr):
    g = arr[0]
    for i in arr:
        g = gcd(g, i)
    return g

def getMyDivisor(n):
	lst = []
	for i in range(1, int(n**(1/2))+1):
		if (n%i == 0):
			lst.append(i)
			if ((i**2) != n) :
				lst.append(n//i)
	lst.sort()
	return lst

def solution(arrayA, arrayB):
    # 철수가 가진 카드를 나눌 수 있고(최대공약수의 약수 리스트) 영희가 가진 카드를 나눌 수 없는 a
    g = gcd_N(arrayA)
    glst = getMyDivisor(g)
    rm = set()
    for num in glst:
        for b in arrayB:
            if b % num == 0:
                rm.add(num)
    
    if not set(glst)-rm :
        a1 = 0
    else:
        a1 = max(set(glst)-rm)
    
    # 영희가 가진 카드를 나눌 수 있고 철수가 가진 카드를 나눌 수 없는 a 최대
    g2 = gcd_N(arrayB)
    glst2 = getMyDivisor(g2)
    rm2 = set()
    for num in glst2:
        for a in arrayA:
            if a%num == 0:
                rm2.add(num)
    if not set(glst2)-rm2 :
        a2 = 0
    else:
        a2 = max(set(glst2)-rm2)
    
    return max(a1, a2)