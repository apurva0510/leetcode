class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = [None]*n
        for i in range (1,len(list)+1):
            if i%3 == 0 and i%5==0:
                list[i-1] = "FizzBuzz"
            elif i%3 == 0:
                list[i-1] = "Fizz"
            elif i%5 == 0:
                list[i-1] = "Buzz"
            else:
                list[i-1] = str(i)

        return list

        