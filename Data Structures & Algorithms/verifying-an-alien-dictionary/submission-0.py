class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c:i for i,c in enumerate(order)}
        return words == sorted(words,key = lambda word : [order_index[c] for c in word])