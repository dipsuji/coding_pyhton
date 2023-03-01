import math


class Solution:
    def count_primes(self, n: int) -> int:

        if n<2:
            return 0
        isPrime = [True]*n
        print(isPrime)
        isPrime[0] = isPrime[1] = False
        print(isPrime)
        ll = math.ceil(math.sqrt(n))
        print(ll)
        for i in range(2,ll):
            if isPrime[i]:
                print("IF IS PRIME----------i --")
                print(i)
                for multiples_of_i in range(i*i,n,i):
                    print("AT THIS POSITION ---- multiples_of_i---")
                    print(multiples_of_i)
                    isPrime[multiples_of_i] = False

        return sum(isPrime)

s = Solution()
answer = s.count_primes(10)
print(answer)