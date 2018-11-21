def collatz(n):
	l=[]
	while(n!=1):
		l.append(n)
		if n%2==0:
			n=n//2
		else:
			n=3*n+1
	l.append(1)
	return l

def n_collatz(n):
    return len(collatz(n))-1

def n_collatz_1(n):
    while (n != 1):
        if n % 2 == 0:
           return n_collatz_1(n//2) +1
        else:
           return n_collatz_1(n*3+1) +1
    else:
        return 0


print(n_collatz_1(25))


