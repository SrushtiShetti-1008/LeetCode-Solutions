class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        i,j=0,len(l)-1
        while i<j:
            if l[i] not in 'aeiouAEIOU':
                i+=1
            if l[j] not in 'aeiouAEIOU':
                j-=1
            if l[i] in 'aeiouAEIOU' and l[j] in 'aeiouAEIOU':
                l[i],l[j] = l[j],l[i]
                i+=1
                j-=1
        return ''.join(l)
