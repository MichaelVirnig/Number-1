def f(y,x,n):#base, exp, mod
	a = x
	c = y
	b = 1
	while a != 0:
		if(a%2 == 0):
			c =(c*c)%n
			a=(a/2)
		else:
			b=(b*c)%n
			a=(a-1)
	return b

def main():
        base = input("Base:  ")
        exp = input("Exponent:  ")
        mod = input("Modulus:  ")
        rem = f(base,exp,mod)
        print("%s^%smod%s = %s" % (base,exp,mod,rem))
main()
