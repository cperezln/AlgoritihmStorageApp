#GDC
'''
    Autor: Admin
    Algorithm to find the greatest common divisor betweent two numbers
'''
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
#Cribe
'''
    Autor: Admin
    Eratostene's cribe, to check the primes between 1 and N
'''
def cribe(n):
	primes = []
	isPrime = [1 for i in range(n)]
	isPrime[0] = isPrime[1] = 0

	for i in range(n):
		if isPrime[i]:
			primes.append(i)
			h = 2
			while i*h < n:
				isPrime[i*h] = 0
				h += 1

	return primes, isPrime