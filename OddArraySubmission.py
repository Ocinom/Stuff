class Solution:
    def sumOddLengthSubarrays(self, arr: [int]) -> int:
        n = len(arr)
        res = 0
		
        for i in range(n):
            even_cnt = ((i // 2) + 1) * ((n - i - 1) // 2 + 1) #not so easy to figure out
            odd_cnt = ((i + 1) // 2) * ((n - i) // 2) #easier to figure out
            res += arr[i] * (even_cnt + odd_cnt) #add arr[i] total count amount of times
            
        return res