word1 = "abcd"
word2 = "pq"

def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        pointer1 = 0
        pointer2 = 0
        new_string = ""
        for i in range(0, len(word1) if len(word1) > len(word2) else len(word2)):
            if pointer1 < len(word1):
                new_string = new_string + word1[pointer1]
            if pointer1 < len(word1):
                  pointer1 = pointer1 + 1
            
            if pointer2 < len(word2):
                new_string = new_string + (word2[pointer2])
            if pointer2 < len(word2):
                  pointer2 = pointer2 + 1
        return new_string


print(mergeAlternately(word1, word2))
