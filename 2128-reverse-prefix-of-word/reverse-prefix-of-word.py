class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = 0
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break
        req_substring = word[0:index+1]
        reverse_substring = req_substring[::-1]
        result = reverse_substring + word[index+1:]
        return result


        