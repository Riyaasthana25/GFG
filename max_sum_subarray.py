class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        start = 0
        end = 0
        sum1 = 0
        ans = 0
        while(end< len(Arr)):
            sum1 += Arr[end]
            if((end - start) + 1 == K):
                ans = max(sum1, ans)
                sum1 -= Arr[start]
                start += 1
            end += 1
        return ans
