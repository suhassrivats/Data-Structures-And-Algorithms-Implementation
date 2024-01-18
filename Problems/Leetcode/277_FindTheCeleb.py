# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Assume the first person is a potential candidate to be a celebrity
        potential_celeb = 0

        for i in range(1, n):
            # A celeb can't know anyone. If candidate knows, update the candidate to the next person
            if knows(potential_celeb, i):
                potential_celeb = i

        # We need this because, we are only checking the current candidate with furture candidate but this candidate shouldn't even know previous candidates. Ex: 1,2,3,4,5 if candidate=4, we are comparing with 5 but not with 1,2,3
        if self.is_celeb(potential_celeb, n):
            return potential_celeb
        else:
            return -1

    def is_celeb(self, potential_celeb, n):
        for i in range(n):
            if i == potential_celeb:
                continue
            # If anyone does now know celeb or celeb knows anyone then he is not a celeb
            if not knows(i, potential_celeb) or knows(potential_celeb, i):
                return False
        return True