class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        d1 = {v: i for i, v in enumerate(list1)}
        dc = {}

        for i, v in enumerate(list2):
            # If resturant exists in list1, find the sum of its indexes and
            # store it in a dictionary (dc). The dictionary values will look
            # like i1+i2:[v1,...].
            if v in d1:
                dc[d1[v] + i] = dc.get(d1[v]+i, []) + [v]

        return dc[min(dc)]
