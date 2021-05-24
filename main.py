class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        wordLen = 0

        for i in words:
            bool = False
            for j in i:
                if j in chars and chars.count(j) >= i.count(j):
                    bool = True
                else:
                    bool = False
                    break
            if bool == True:
                wordLen += len(i)

        return wordLen

# ===============

