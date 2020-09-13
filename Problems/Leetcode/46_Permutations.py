class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.dfs(nums, [], results)
        return results

    def results(self, nums, path, results):
        if not nums:
            results.append(path)

        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], results)
