class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)<=len(word2):
            small = word1
        else:
            small = word2

        res=''
        for i in range(len(small)):
            res += word1[i] + word2[i]
        res=res+word1[i+1:]+word2[i+1:]
        return res
        