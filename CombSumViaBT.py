class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        def backtracking(remain, path, index):
            if remain == 0:
                res.append(path)

            for i in range(index, len(candidates)):
                if candidates[i] > remain:
                    break

                backtracking(remain - candidates[i], path + [candidates[i]], i)

        candidates.sort()
        res = []
        path = []
        index = 0

        backtracking(target, path, index)

        return res