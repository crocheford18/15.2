#Euler 50
import time

start_time = time.clock()
i = 6
# this sets the first number at 6
numbers = []
primes = []
#this creates separates lists for numbers and primes
while sum(numbers) < 1000000-i:
	digits = map(int, range(2, i))
#when the sum of numbers is less than 1000000-i this will create a list out of the numbers from 2 up to
#but not including i
	digits[:] = [i % x for x in digits]
#this puts the remainder of i / all numbers in digits into an updated digits list
	from operator import mul
	p = reduce(mul, digits, 1)
#this multiplies all the numbers in digits together to get the product (p)
	if p == 0:
#		print "Nope"
#if p is 0 these numbers aren't prime because some number went into i perfectly and had 0 remaining
#since there was at least one zero in that number the product would be 0 and it isn't prime
		i = i + 1
#this adds one to whatever number i was and goes back to making a list of numbers
	else:
		numbers.append(i)
#this adds i to numbers because i is prime (product did not equal 0)
		primes.append(1)
#this adds 1 to primes because it was a prime number and we want to know how many primes are in the sum
		i = i + 1

print "The highest prime number under 1,000,000 consisting of the sum of consecutive prime numbers is: %d" % (sum(numbers))
#this prints the sum of numbers which is all the prime numbers added up together
print "The number of consecutive primes in that number are: %d"  % (sum(primes))
#this gives the number of primes that it took to get to the number mentioned above
print time.clock() - start_time, "seconds"
