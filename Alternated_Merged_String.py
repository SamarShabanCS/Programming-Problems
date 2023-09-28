'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

'''


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1 = 0
        ptr2 = 0

        lenStr1 = len(word1)
        lenStr2 = len(word2)
        mergedString = ''
        while(ptr1<lenStr1 and ptr2<lenStr2):
            mergedString += word1[ptr1] + word2[ptr2]
            ptr1 += 1
            ptr2 += 1
        if ptr1 < lenStr1:
            mergedString += word1[ptr1:]
        if ptr2 < lenStr2:
            mergedString += word2[ptr2:]
         
        # return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))
        return mergedString
   
