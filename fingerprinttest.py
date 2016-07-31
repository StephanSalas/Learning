<<<<<<< HEAD
import random

def createRandomArray(arrLen,lb,ub):
	random.seed(1024);
	random.seed(591);
	random.seed(100);
	return [random.randint(lb,ub) for _ in range(arrLen)];

def test_fingerprint(m,T,r): 		
	# print(m)
	assert (m > 255) & (r > 1) & (r < m - 1);
	fp = (T[1] * r) % m;
	for i in range(2,len(T)):
		fp = ((fp + T[i]) * r) % m;
	return fp;

def FingerprintTexts(inputStr1,inputStr2):
	return true; 
	# TO DO

def inputAsserations(inputStr1,inputStr2):
	return true;
	# TO DO



T = createRandomArray(10000,1,255);
M = len(T) * 10;
rk = createRandomArray(10,1,M-1);

for i in range(1,len(rk)):
	print(str(test_fingerprint(M,T,rk[i]))); # Replace with Auth
	print(str(test_fingerprint(M,T,rk[i]))); # Replace with Adversary
=======
import random

def createRandomArray(arrLen,lb,ub):
	random.seed(1024)
	random.seed(591)
	random.seed(100)
	return [random.randint(lb,ub) for _ in range(arrLen)]	

def fingerprint(m,T,r): 		
	# print(m)
	assert (m > 255) & (r > 1) & (r < m - 1) 
	fp = (T[1] * r) % m
	for i in range(2,len(T)):
		fp = ((fp + T[i]) * r) % m
	return fp


T = createRandomArray(10000,1,255)
M = len(T) * 10
rk = createRandomArray(10,1,M-1);
print(len(rk))

for i in range(1,len(rk)):
	print(str(fingerprint(M,T,rk[i]))) # Replace with Auth
	print(str(fingerprint(M,T,rk[i]))) # Replace with Adversary
>>>>>>> 3d944ac08fe98a8c64be22ea2907a8111ea458ac
		