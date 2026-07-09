class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        
        if len1 + len2 != len3:
            return False
        
        dp = [False] * (len2 + 1)
        
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or \
                            (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                            
        return dp[len2]