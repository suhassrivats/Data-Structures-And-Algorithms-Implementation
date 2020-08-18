class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []

        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                results.append("FizzBuzz")
            elif num % 3 == 0:
                results.append("Fizz")
            elif num % 5 == 0:
                results.append("Buzz")
            else:
                results.append(str(num))

        return results
