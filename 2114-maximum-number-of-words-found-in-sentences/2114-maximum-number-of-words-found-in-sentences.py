class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(word.split(" ")) for word in sentences)
    
    """temp = []
        abc = []
        for i in range(len(sentences)):
            temp = sentences[i].split(" ")
            abc.append(len(temp))
        return max(abc) """
            