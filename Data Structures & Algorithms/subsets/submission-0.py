class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = []

        def backtrack(i):
            if i == n:
                # Don't pass the reference to sol, since you dont want to modify it, pass the snapshot of it sol[:]
                res.append(sol[:])
                return 
            # Dont pick nums[i]
            backtrack(i + 1)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)

            # Undo the changes
            sol.pop()


        backtrack(0)
        return res